import threading
import time
from yt_dlp import YoutubeDL
from SQLManager import SQLManager


class Recorder(threading.Thread):
    def __init__(self, streamer_id: str):
        super().__init__()
        self.streamer_id = streamer_id
        self.TWITCH_URL = "https://www.twitch.tv/"
        self.ydl_opts = {
            "external_downloader_args": ["-loglevel", "panic"],
            "outtmpl": "videos/" + streamer_id + "/%(title)s.%(ext)s",
            "format": "bestvideo+bestaudio/best",
            "nooverwrites": True,
            # "restrictfilenames": True, # 한글 및 공백 제거
            "quiet": True,
        }

    def run(self):
        print("start record: " + self.streamer_id)

        with YoutubeDL(self.ydl_opts) as ydl:
            while True:
                try:
                    ydl.download([self.TWITCH_URL + self.streamer_id])
                except:
                    # print("not currently live")
                    time.sleep(30)


def main():
    recorder = Recorder("slientear")
    recorder.start()


if __name__ == "__main__":
    main()
