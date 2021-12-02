import sqlite3, psycopg2
from werkzeug.security import generate_password_hash


def populate_admin_to_db(ENV, id: int, email: str, password: str, user_name: str, game_id: int, admin: bool):
    try:
        print("--adding a super user--")
        if ENV == "DEV":
            connect = sqlite3.connect("test.db")
        else:
            db_connection_url = "postgres://isjsgcztftfslw:74317591be27ee99df92e8860a110f5cf7f6ed0d26719378815c8e554bf3a521@ec2-23-23-219-25.compute-1.amazonaws.com:5432/dfrqcekr8skvl"
            connect = psycopg2.connect(db_connection_url)
        cur = connect.cursor()
        print("--Connected to Database Succesfully--")
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(cur.fetchall())
        password_hash = generate_password_hash(password, method='sha256')
        admin_info = [id, email, password_hash, user_name, game_id, admin]
        
        print("Adding a Super User!")
        
        cur.execute('INSERT INTO "Player" (id, email, password, player_name, game_id, admin) VALUES (?, ?, ?, ?, ?, ?);', admin_info)
        connect.commit()
        print("SUPER USER HAS BEEN ADDED!")
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(cur.fetchall())
        connect.close()

    except Exception as e:
        print(e)
        print("An Error has occurd during generate admin account!")
