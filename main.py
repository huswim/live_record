import threading
from yt_dlp import YoutubeDL
import time

TWITCH_URL = "https://www.twitch.tv/"
streamer_id_list: list[str] = ["woowakgood", "lilpaaaaaa", "gosegugosegu"]
thread_list: list[threading.Thread] = []


def record(streamer_id: str):
    print("start record: " + streamer_id)

    with YoutubeDL() as ydl:
        ydl.download([TWITCH_URL + streamer_id])

    print("end record: " + streamer_id)


def record_all():
    # streamer id list에 있는 모든 스트리머를 동시에 녹화
    print("start record all")
    for streamer_id in streamer_id_list:
        t_temp = threading.Thread(target=record, args=(streamer_id,))
        thread_list.append(t_temp)
        t_temp.start()


def main():
    record_all()

    while True:
        for th in thread_list:
            if not th.is_alive():
                th.start()
        time.sleep(20)


if __name__ == "__main__":
    main()
