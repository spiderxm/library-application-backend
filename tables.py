import pymysql.cursors

mydb = pymysql.connect(
    host='34.71.242.51',
    user='root',
    password='100pipers',
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)

try:
    mycursor = mydb.cursor()
    print("Cursor created")
except:
    print("Error creating cursor")
# creating database
try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS LIBRARY")
    print("Database library created")
except:
    print("Error creating database")
# using library database
try:
    mycursor.execute("USE LIBRARY")
    print("Entered into LIBRARY Database")
except:
    print("Error using library database")
# creating table
# author name, date, department,status
try:
    query = "CREATE TABLE IF NOT EXISTS books(" \
            "book_id varchar(20) NOT NULL primary key, " \
            "user_id varchar(50) NOT NULL, " \
            "book_name varchar(50) NOT NULL, " \
            "status varchar(10) NOT NULL, " \
            "issue_date timestamp DEFAULT current_timestamp NOT NULL , " \
            "author_name VARCHAR(30) NOT NULL, " \
            "department varchar(20) NOT NULL" \
            ")"
    mycursor.execute(query)
    print("Table created")
except:
    print("Error in creating books table")

mycursor.close()
mydb.close()
