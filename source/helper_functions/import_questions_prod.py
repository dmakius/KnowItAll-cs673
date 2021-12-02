import psycopg2, os
import pandas as pd

db_connection_url = "postgres://isjsgcztftfslw:74317591be27ee99df92e8860a110f5cf7f6ed0d26719378815c8e554bf3a521@ec2-23-23-219-25.compute-1.amazonaws.com:5432/dfrqcekr8skvl"

def populate_db_prod():
    try:
      
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(db_connection_url)
        print("Connection successful")
        cursor = conn.cursor()
       
        os.chdir('../')
        df = pd.read_csv("Quiz_Questions.csv", encoding="ISO-8859-1")
        print("SUCESSFULLY OPENED CSV FILE!")
        for index, row in df.iterrows():
            print(index)
            query = 'INSERT INTO "Question" (id, category, question, answer, option_1, option_2, option_3) VALUES (%s,%s, %s, %s, %s, %s, %s);'
            data = (
            index, row['Category'], row['Question'], row['Answer'], row['Option_1'], row['Option_2'], row['Option_3'])
            cursor.execute(query, data)
            conn.commit()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
