#!C:/Python36-32/python.exe

import pymysql
import cgi

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='fb_register', autocommit=True)

cursor = connection.cursor()

form = cgi.FieldStorage()
u_name = form.getvalue("u_name")
mail = form.getvalue("u_mail")
pwd = form.getvalue("u_pwd")

def print_html():

    # print(name)

    print("""
    <!DOCTYPE html>
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
    <h1>Registered Successfully </h1>
    </body>
    </html>
    """)


def exec_query():

    query = "INSERT INTO my_table (name,email,password) VALUES (%s,%s,%s)"

    cursor.execute(query, (u_name,mail,pwd))

    print_html()

exec_query()

