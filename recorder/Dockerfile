FROM alpine:3

RUN apk update
RUN apk add ffmpeg python3 py3-pip
RUN pip install yt-dlp

RUN mkdir -p /app
RUN mkdir -p /app/videos
WORKDIR /app/videos

ADD main.py /app

CMD ["python", "../main.py"]
