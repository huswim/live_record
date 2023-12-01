from Recorder import RecorderManager


TWITCH_URL = "https://www.twitch.tv/"


def main():
    manager = RecorderManager("streamers.db")
    manager.start()


if __name__ == "__main__":
    main()
