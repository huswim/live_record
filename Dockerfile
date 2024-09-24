FROM alpine:3

RUN apk update
RUN apk add ffmpeg yt-dlp

RUN mkdir -p /app/videos

WORKDIR /app
COPY ./run.sh /app
RUN chmod +x ./run.sh

WORKDIR /app/videos

CMD [ "../run.sh" ]