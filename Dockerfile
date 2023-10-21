FROM python:3.12

RUN apt-get update
RUN apt-get install -y ffmpeg
RUN pip install yt-dlp

RUN mkdir -p /app
RUN mkdir -p /app/videos
WORKDIR /app/videos

ADD main.py /app

CMD ["python", "../main.py"]
