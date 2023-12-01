from Recorder import RecorderManager
from SQLManager import SQLManager

streamer_id_list: list[str] = [
    "vo_ine",
    "jingburger",
    "lilpaaaaaa",
    "cotton__123",
    "gosegugosegu",
    "viichan6",
]


def main():
    sql_manager = SQLManager("streamers.db")
    for streamer_id in streamer_id_list:
        sql_manager.add_streamer_id(streamer_id)
    

    manager = RecorderManager("streamers.db")
    manager.start()


if __name__ == "__main__":
    main()
