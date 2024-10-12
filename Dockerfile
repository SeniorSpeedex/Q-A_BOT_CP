FROM ollama:lastest

RUN apt-get update && apt-get install -y bash

COPY entrypoint.sh /root/entrypoint.sh
RUN chmod +x /root/entrypoint.sh
