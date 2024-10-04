import asyncio
import os
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter
from typing import override, final

import whisper
from ffmpeg.asyncio import FFmpeg

from app.bot import logger
from app.bot.api.stt.base_stt import BaseSpeechToText
from app.bot.config import available_stt_models, available_stt_languages


@final
class SpeechToText(BaseSpeechToText):
    def __init__(self, input_file: str, model: available_stt_models = "base", language: available_stt_languages = "ru"):
        self.wav_file = None
        self.__audio_extracted = False
        super().__init__(input_file, model, language)

    @override
    async def transcribe(self) -> str:
        """
        Transcribe the audio content from the input file.

        :return: Transcribed text as a string.
        """
        if not self.__audio_extracted:
            await self.extract_audio_from_video()

        if self.wav_file is None:
            raise ValueError("wav_file is not set")

        start_time = perf_counter()

        loop = asyncio.get_running_loop()
        with ThreadPoolExecutor() as pool:
            result = await loop.run_in_executor(pool, self._transcribe_in_thread)

        logger.info(f"The full transcription of the video took {perf_counter() - start_time}")

        return result['text']

    def _transcribe_in_thread(self):
        model = whisper.load_model(self.model)
        return model.transcribe(self.wav_file, language=self.language)

    @override
    async def extract_audio_from_video(self) -> None:
        """
        Extract audio from the input video file.

        :return: None
        """
        wav_file = os.path.splitext(self.input_file)[0] + '.wav'
        ffmpeg = (
            FFmpeg()
            .option("y")
            .input(self.input_file)
            .output(
                wav_file,
                acodec="pcm_s16le",
                ar=16000
            )
        )
        await ffmpeg.execute()
        self.wav_file = wav_file
        self.__audio_extracted = True
