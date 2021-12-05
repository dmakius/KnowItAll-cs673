import psycopg2
db_connection_url="postgres://lanjgohxxeslei:c01c189ac2d6bba85d69ffd51a2e2c1159a3399b73f3750b1771c85bdb892077@ec2-44-193-111-218.compute-1.amazonaws.com:5432/d1rq51phecr4k2"
print('Connecting to the PostgreSQL database...')
conn = psycopg2.connect(db_connection_url)
print("Connection successful")
cursor = conn.cursor()

# cursor.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
# x = cursor.fetchall()
# print(x)
cursor.execute('SELECT * FROM "Question" order by id')
x = cursor.fetchall()
for y in x:
    print(y)

user_id=7
cursor.execute(''' SELECT category, MAX(score) FROM "LeaderboardScore" where userid = '%s' group by category ''', [user_id] )
z = cursor.fetchall()
for y in z:
    print(y)