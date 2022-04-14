FROM python:3.7-alpine

RUN mkdir /honeypot
WORKDIR /honeypot

USER honeypot

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["bash"]
CMD ["-c", "/honeypot/start_honeypot.sh"]
