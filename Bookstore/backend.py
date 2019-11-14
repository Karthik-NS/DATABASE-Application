import mysql.connector

def connect():
    con = mysql.connector.connect(host="localhost", user="root", password="1234")
    cur = con.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS bookstore")
    cur.execute("USE bookstore")
    cur.execute("CREATE TABLE IF NOT EXISTS books( title text, author text, year integer, isbn BIGINT PRIMARY KEY)")
    con.commit()
    cur.close()
    con.close()

def insert(isbn,title='',author='',year=''):
    con = mysql.connector.connect(host="localhost", user="root", password="1234", database="bookstore")
    cur = con.cursor()
    cur.execute("INSERT INTO books VALUES('%s','%s','%s','%s')" %(title,author,year,isbn))
    con.commit()
    cur.close()
    con.close()

def view():
    con = mysql.connector.connect(host="localhost", user="root", password="1234", database= "bookstore")
    cur = con.cursor()
    cur.execute("SELECT * FROM books")
    rows =cur.fetchall()
    cur.close()
    con.close()
    return rows

def search(title="",author="",year="",isbn=""):
    con = mysql.connector.connect(host="localhost", user="root", password="1234", database= "bookstore")
    cur = con.cursor()
    cur.execute("SELECT * FROM books WHERE title = '%s' or author= '%s' or year='%s' or isbn='%s'" %(title,author,year,isbn))
    row = cur.fetchall()
    cur.close()
    con.close()
    return row


def update(isbn,title='',author='',year=0):
    con = mysql.connector.connect(host="localhost", user="root", password="1234", database="bookstore")
    cur = con.cursor()
    cur.execute("SELECT * FROM books WHERE isbn=%i" %isbn)
    title2,author2,year2,isbn2 = cur.fetchone()
    if title=='':
        title=title2  # keeping same title if user has not entered any value
    if author=='':
        author=author2  # keeping same author if user has not entered any value
    if year==0:
        year=year2  # keeping same year if user has not entered any value
    cur.execute("UPDATE books SET title = '%s', author= '%s', year ='%s' WHERE isbn=%i " %(title,author,year,isbn))
    con.commit()
    cur.close()
    con.close()

def delete(isbn):
    con = mysql.connector.connect(host="localhost", user="root", password="1234", database="bookstore")
    cur = con.cursor()
    cur.execute("DELETE FROM books WHERE isbn=%i" %isbn)
    con.commit()
    cur.close()
    con.close()


connect()



update(2459783,author='SAHAS')