#!/usr/bin/sh

ollama serve &

sleep 5

ollama pull qwen2:1.5b
ollama run qwen2:1.5b

wait
