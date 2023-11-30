import threading
from yt_dlp import YoutubeDL
import time

TWITCH_URL = "https://www.twitch.tv/"
streamer_id_list: list[str] = [
    "vo_ine",
    "jingburger",
    "lilpaaaaaa",
    "cotton__123",
    "gosegugosegu",
    "viichan6",
]
thread_list: list[threading.Thread] = []


def record(streamer_id: str):
    print("start record: " + streamer_id)

    with YoutubeDL() as ydl:
        while True:
            try:
                ydl.download([TWITCH_URL + streamer_id])
            except:
                print("not currently live")
                time.sleep(30)


def main():
    for streamer_id in streamer_id_list:
        t_temp = threading.Thread(target=record, args=(streamer_id,))
        thread_list.append(t_temp)
        t_temp.start()


if __name__ == "__main__":
    main()
