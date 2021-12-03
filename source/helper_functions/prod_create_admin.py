import psycopg2 , os
from sqlalchemy.sql.expression import null
from werkzeug.security import generate_password_hash

db_connection_url = os.environ['DATABASE_URL'].replace("://", "ql://", 1)

print('Connecting to the PostgreSQL database...')
conn = psycopg2.connect(db_connection_url)
cursor = conn.cursor()

email = 'admin@test.com'
password= "admin1234"
password_hash = generate_password_hash(password, method='sha256')
player_name='admin'
print("HASH PASSWORD: " + str(password_hash))

add_info = (1, email, password_hash, player_name, 1, True )
cursor.execute('INSERT INTO "Player" (id, email, password, player_name, game_id, admin) VALUES (%s, %s, %s, %s, %s, %s)', add_info)
conn.commit()
cursor.close()