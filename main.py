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
    "viichan6"
]
thread_list: list[threading.Thread] = []


def record(streamer_id: str):
    print("start record: " + streamer_id)

    while True:
        with YoutubeDL() as ydl:
            try:
                ydl.download([TWITCH_URL + streamer_id])
                break
            except:
                print("not currently live")
                time.sleep(5)

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
        for idx, th in enumerate(thread_list):
            if not th.is_alive():
                thread_list[idx] = threading.Thread(
                    target=record, args=(streamer_id_list[idx],)
                )


if __name__ == "__main__":
    main()
