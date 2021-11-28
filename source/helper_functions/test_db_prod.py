import psycopg2, os
def db_exists():
    try:
        db_connection_url="postgres://isjsgcztftfslw:74317591be27ee99df92e8860a110f5cf7f6ed0d26719378815c8e554bf3a521@ec2-23-23-219-25.compute-1.amazonaws.com:5432/dfrqcekr8skvl"
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