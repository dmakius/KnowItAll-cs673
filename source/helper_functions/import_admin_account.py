import sqlite3, psycopg2
from werkzeug.security import generate_password_hash


def populate_admin_to_db(id: int, email: str, password: str, user_name: str, game_id: int, admin: bool):
    try:

        connect = sqlite3.connect("test.db")
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
 
 
        connect.close()

    except Exception as e:
        print(e)
        print("An Error has occurd during generate admin account!")
