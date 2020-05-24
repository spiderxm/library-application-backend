import pymysql.cursors

mydb = pymysql.connect(
    host='bank.ct1ikgzgdh96.us-east-1.rds.amazonaws.com',
    user='admin',
    password='adminadmin',
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
            "book_id varchar(20) PRIMARY KEY , " \
            "user_id varchar(50) NOT NULL, " \
            "book_name varchar(50) NOT NULL, " \
            "status varchar(10) NOT NULL, " \
            "issue_date timestamp DEFAULT current_timestamp, " \
            "author_name VARCHAR(30) NOT NULL, " \
            "department varchar(20) NOT NULL, " \
            "issue_status varchar(20) NOT NULL" \
            ")"
    mycursor.execute(query)
    print("Table created")
except:
    print("Error in creating books table")

mycursor.close()
mydb.close()