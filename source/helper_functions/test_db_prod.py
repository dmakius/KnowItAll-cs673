import psycopg2, os
def db_exists():
    try:
        db_connection_url="postgres://wfruzqxzgniqgt:44d774b175af6321ef93bd8e1555e07f12c228721f71de9449be228b1d57dca4@ec2-54-235-45-88.compute-1.amazonaws.com:5432/d65sfgg636vqua"
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(db_connection_url)
        print("Connection successful")
        cursor = conn.cursor()

        cursor.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
        x = cursor.fetchall()

        if len(x) == 0:
            return False
        else:
            return True

    except (Exception, psycopg2.DatabaseError) as error:
        print("An Error has occurd!")
        print(error)