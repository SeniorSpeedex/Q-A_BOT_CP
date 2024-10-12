FROM ollama/ollama

RUN apt-get update && apt-get install -y bash

COPY /root/entrypoint.sh entrypoint.sh
RUN chmod +x /root/entrypoint.sh
