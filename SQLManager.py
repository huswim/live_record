import sqlite3
import sys


class SQLManager:
    def __init__(self, db_name: str) -> None:
        self.con = sqlite3.connect(db_name)
        self.create_streamer_id_table()

    def create_streamer_id_table(self):
        cur = self.con.cursor()

        try:
            cur.execute("CREATE TABLE STREAMERS(id text PRIMARY KEY)")
            self.con.commit()
        except sqlite3.OperationalError:
            # If table already exists
            print(f'Warning : table "STREAMERS" already exists')
            pass

    def add_streamer_id(self, streamer_id: str):
        cur = self.con.cursor()
        try:
            cur.execute("INSERT INTO STREAMERS VALUES (?)", (streamer_id,))
            self.con.commit()
        except sqlite3.IntegrityError:
            # If streamer_id already exists
            print(f'Warning : streamer_id "{streamer_id}" already exists')
            pass

    def remove_streamer_id(self, streamer_id: str):
        cur = self.con.cursor()

        cur.execute("DELETE FROM STREAMERS WHERE id=?", (streamer_id,))
        self.con.commit()

    def get_streamer_ids(self) -> list:
        cur = self.con.cursor()

        cur.execute("SELECT * FROM STREAMERS")
        #  cur.fetchall() to list[str]
        return [streamer_id[0] for streamer_id in cur.fetchall()]


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "show":
        manager = SQLManager("streamers.db")
        print(manager.get_streamer_ids())
        return

    if len(sys.argv) != 3:
        print("Usage: python SQLManager.py [add/remove] [streamer_id]")
        print("Usage: python SQLManager.py show")
        return

    option = sys.argv[1]
    streamer_id = sys.argv[2]

    manager = SQLManager("streamers.db")

    if option == "add":
        manager.add_streamer_id(streamer_id)

    elif option == "remove":
        manager.remove_streamer_id(streamer_id)

    else:
        print("Usage: python SQLManager.py [add/remove] [streamer_id]")
        print("Usage: python SQLManager.py show")
        return


if __name__ == "__main__":
    main()
