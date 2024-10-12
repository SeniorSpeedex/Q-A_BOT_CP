FROM ollama/ollama

RUN apt-get update && apt-get install -y bash

COPY entrypoint.sh /root/entrypoint.sh
RUN chmod +x /root/entrypoint.sh
RUN ollama serve & sleep 5 && ollama pull qwen2:7b-instruct-fp16