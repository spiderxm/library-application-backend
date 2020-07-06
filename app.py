from flask import Flask, request, jsonify
import pymysql.cursors
from flask_cors import CORS
from datetime import datetime
app = Flask(__name__)
CORS(app)
try:
    mydb = pymysql.connect(
        host='34.71.242.51',
        user='root',
        password='100pipers',
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
        print(user_id)
        query = "SELECT * FROM books where user_id = '{}' and status = 'issued'".format(user_id)
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
        query = "SELECT * FROM books where user_id = '{}' and status = 'returned'".format(user_id)
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


@app.route('/add_book', methods=['POST'])
def add_book():
    try:
        data = request.json
        print(data)
        user_id = data['user_id']
        book_id = data['book_id']
        book_name = data['book_name']
        status = data['status']
        issue_date = data['issue_date']
        author_name = data['author_name']
        department = data['department']
        issue_date = datetime.strptime(issue_date,'%Y-%m-%d')
        query = "INSERT INTO books(book_id,user_id,book_name,status,issue_date,author_name,department) values " \
                "(" \
                "'{}'," \
                "'{}'," \
                "'{}'," \
                "'{}'," \
                "'{}'," \
                "'{}'," \
                "'{}'" \
                ")".format(book_id,
                           user_id,
                           book_name,
                           status,
                           issue_date,
                           author_name,
                           department)
        print(query)
        mycursor.execute(query)
        return jsonify({
            "status_code": 200,
            "message": "Book successfully entered",
            "book_id": book_id,
            "user_id": user_id
        })
    except Exception as e:
        print(e)
        return jsonify({
            "status_code": 200,
            "error": "Book was not entered"
        })


@app.route('/deletebook/<string:userid>/<string:bookid>', methods=['Delete'])
def delete_books(userid, bookid):
    try:
        user_id = userid
        book_id = bookid
        query = "UPDATE books SET status = 'returned' where user_id = '{}' and book_id = '{}'".format(user_id, book_id)
        print(query)
        mycursor.execute(query)
        return jsonify({
            "status_code": 200,
            "message": "Book was successfully returned"
        })
    except:
        print("Error")
        return jsonify({
            "status_code": 200,
            "error": "Book was not deleted"
        })


if __name__ == '__main__':
    app.run()
