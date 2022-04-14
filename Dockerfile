FROM python:3.7-alpine
WORKDIR /honeypot

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["bash"]
CMD ["-c", "/honeypot/start_honeypot.sh"]
