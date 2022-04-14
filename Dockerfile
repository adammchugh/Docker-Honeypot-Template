FROM python:3.7-alpine
WORKDIR /code

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["bash"]
CMD ["-c", "/code/start_honeypot.sh"]
