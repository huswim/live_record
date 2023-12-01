from Recorder import RecorderManager


def main():
    manager = RecorderManager("streamers.db")
    manager.start()


if __name__ == "__main__":
    main()
