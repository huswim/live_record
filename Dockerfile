FROM alpine:3

RUN apk update
RUN apk add ffmpeg python3 py3-pip
RUN pip install yt-dlp

RUN mkdir -p /app/src
RUN mkdir -p /app/videos
WORKDIR /app

ADD ./src/*.py /app/src/

CMD ["python", "/app/src/main.py"]
