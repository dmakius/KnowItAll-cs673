import sqlite3
from werkzeug.security import generate_password_hash


def populate_admin_to_db(id: int, email: str, password: str, user_name: str, game_id: int, admin: bool):
    try:
        connect = sqlite3.connect("test.db")
        cur = connect.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(cur.fetchall())
        password_hash = generate_password_hash(password, method='sha256')
        admin_info = [id, email, password_hash, user_name, game_id, admin]
        cur.execute("INSERT INTO player (id, email, password, player_name, game_id, admin) VALUES (?, ?, ?, ?, ?, ?);",
                    admin_info)
        connect.commit()
        print("Data base has sucesfully been populated")
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(cur.fetchall())
        connect.close()

    except Exception as e:
        print(e)
        print("An Error has occurd during generate admin account!")
