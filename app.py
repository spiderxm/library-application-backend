from flask import Flask, request, jsonify
import pymysql.cursors

app = Flask(__name__)
try:
    mydb = pymysql.connect(
        host='bank.ct1ikgzgdh96.us-east-1.rds.amazonaws.com',
        user='admin',
        password='adminadmin',
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )
except:
    print("Error connecting to mysql server")

try:
    mycursor = mydb.cursor()
    print("Cursor created")
except:
    print("Error creating cursor")

# using library database
try:
    mycursor.execute("USE LIBRARY")
    print("Entered into LIBRARY Database")
except:
    print("Error using library database")


@app.route('/books/<string:user_id>')
def books(user_id):
    try:
        query = "SELECT * FROM books where user_id = '{}'".format(user_id)
        mycursor.execute(query)
        book_details = []
        book_detail = mycursor.fetchone()
        while book_detail:
            book_details.append(book_detail)
            book_detail = mycursor.fetchone()
        return jsonify(book_details)
    except:
        return jsonify({
            "status_code": 200,
            "error": "user_id does not exist or is incorrect please try again"
        })


@app.route('/issued_books/<string:user_id>')
def currently_issued_books(user_id):
    try:
        query = "SELECT * FROM books where user_id = '{}' and issue_status = 'issued'".format(user_id)
        mycursor.execute(query)
        book_details = []
        book_detail = mycursor.fetchone()
        while book_detail:
            book_details.append(book_detail)
            book_detail = mycursor.fetchone()
        return jsonify(book_details)
    except:
        return jsonify({
            "status_code": 200,
            "error": "user_id does not exist or is incorrect please try again"
        })


@app.route('/returned_books/<string:user_id>')
def returned_books(user_id):
    try:
        query = "SELECT * FROM books where user_id = '{}' and issue_status = 'returned'".format(user_id)
        mycursor.execute(query)
        book_details = []
        book_detail = mycursor.fetchone()
        while book_detail:
            book_details.append(book_detail)
            book_detail = mycursor.fetchone()
        return jsonify(book_details)
    except:
        return jsonify({
            "status_code": 200,
            "error": "user_id does not exist or is incorrect please try again"
        })


if __name__ == '__main__':
    app.run()
