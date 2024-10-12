FROM ollama/ollama

COPY entrypoint.sh /root/entrypoint.sh
RUN chmod +x /root/entrypoint.sh
