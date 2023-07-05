FROM python:3.10-slim

RUN apt-get update -y && apt-get install -y sqlite3
RUN pip install requests==2.31.0 lxml==4.9.3

COPY . /bot
WORKDIR /bot
ENTRYPOINT [ "python", "bot.py" ]
