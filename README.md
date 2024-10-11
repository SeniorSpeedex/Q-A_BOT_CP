# Q-A Bot CP

Этот проект представляет собой Telegram-бота, созданного с использованием асинхронного фреймворка aiogram. Он предназначен для взаимодействия с пользователями и использует сервисы на базе искусственного интеллекта (через "Ollama") для расширения функциональности. Бот упакован в контейнер с использованием Docker и поддерживает графический процессор NVIDIA GPU runtime для высокопроизводительного вывода модели искусственного интеллекта.

## Требования
- Докер
- Поддержка bash скриптов (опционально)

## Технологический стэк
- Python 3.12
- Aiogram - Асинхронная библиотека для работы с апи телеграмма
- Aiohttp - Используем асинхронный клиент
- Asyncio - Асинхронный рантайм
- - -
- Ollama API
- Qwen2:70b (LLM)
- Whisper-base (STT)

## Быстрое развертывание с помощью bash
- После клонирования нужно будет установить токен боту в .env
```bash
git clone https://github.com/SeniorSpeedex/Q-A_BOT_CP && \
mv Q-A_BOT_CP/setup.sh . && \
sh setup.sh && \
cd Q-A_BOT_CP && \
sh nv-runtime-setup.sh
```
- Затем перезагрузим систему
```bash
sudo reboot
```
- Для первичной установки нейросети в контейнер используем
```bash
cd Q-A_BOT_CP && \
docker compose up --build
```


## Особенности
- **Telegram-бот**: Взаимодействует с пользователями с помощью команд и сообщений.
- **Интеграция с ИИ**: Использование моделей ИИ через контейнер Ollama для обработки запросов.
- **Dockerized**: Простое развертывание с использованием Docker Compose и поддержкой графического процессора для вывода ИИ.

## TODO
- Улучшение UI
- Больше киллер-фич