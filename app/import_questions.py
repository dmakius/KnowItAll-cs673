import csv, sqlite3

# connec to DB
con = sqlite3.connect("test.db")  # change to 'sqlite:///your_filename.db'
cur = con.cursor()

# If Question Table exists , DROP the Table and DROP a new one
cur.execute("DROP TABLE question")
cur.execute(
    "CREATE TABLE question (ID, Category, Question, Answer, Option_1, Option_2, Option_3);")  # use your column names here

# OPEN csv file and
with open('Quiz_Questions.csv', encoding='ISO-8859-1') as fin:  # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin)  # comma is default delimiter
    to_db = [(i['ID'], i['Category'], i['Question'], i['Answer'], i['Option_1'], i['Option_2'], i['Option_3']) for i in
             dr]

cur.executemany(
    "INSERT INTO question (ID,Category,Question,Answer,Option_1,Option_2,Option_3) VALUES (?, ?, ?, ?, ?, ?,?);", to_db)
con.commit()
con.close()
