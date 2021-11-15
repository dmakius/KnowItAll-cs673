import psycopg2, csv
import pandas as pd

db_connection_url="postgres://qoigszfjzslytb:ed69522773e0bc17f93775cae0c84ed20ad3a255905cde3902feb9536e166c33@ec2-52-203-27-62.compute-1.amazonaws.com:5432/depmssv4b61llt"

try:
    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(db_connection_url)
    print("Connection successful")
    cursor = conn.cursor()
    cursor.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
    for table in cursor.fetchall():
        print(table)
    # print (cur.fetchall())
    df = pd.read_csv("Quiz_Questions.csv",encoding = "ISO-8859-1")
    for index, row in df.iterrows():
        print(index)
        query =  'INSERT INTO "Question" (id, category, question, answer, option_1, option_2, option_3) VALUES (%s,%s, %s, %s, %s, %s, %s);'
        data = (index, row['Category'], row['Question'], row['Answer'], row['Option_1'], row['Option_2'], row['Option_3'])
        cursor.execute(query, data)
        conn.commit()
    conn.close()
    
except (Exception, psycopg2.DatabaseError) as error:
     print(error)
     
