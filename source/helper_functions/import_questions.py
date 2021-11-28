import csv, sqlite3


def populate_db():
    try:
        # connect to DB
        con = sqlite3.connect("test.db")  # change to 'sqlite:///your_filename.db'
        cur = con.cursor()

        # get the database tables
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(cur.fetchall())

        with open('Quiz_Questions.csv', encoding='ISO-8859-1') as fin:  # `with` statement available in 2.5+
            # csv.DictReader uses first line in file for column headings by default
            print("CSV File OPENED")
            dr = csv.DictReader(fin)  # comma is default delimiter
            to_db = [(i['ID'], i['Category'], i['Question'], i['Answer'], i['Option_1'], i['Option_2'], i['Option_3'])
                     for i in
                     dr]

        cur.executemany(
            "INSERT INTO question (ID,Category,Question,Answer,Option_1,Option_2,Option_3) VALUES (?, ?, ?, ?, ?, ?,?);"
            , to_db)
        con.commit()

        print("Data base has sucesfully been populated")
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(cur.fetchall())
        con.close()
    except Exception as e:
        print(e)
        print("An Error has occurd!")
