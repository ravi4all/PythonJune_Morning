#!C:/Python36-32/python.exe

import pymysql
import cgi

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='fb_register', autocommit=True)

cursor = connection.cursor()

form = cgi.FieldStorage()
mail = form.getvalue("u_mail")
pwd = form.getvalue("u_pwd")

def print_html(name):

    # print(name)

    print("""
    <!DOCTYPE html>
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
    <h1>Hello {} </h1>
    </body>
    </html>
    """.format(name))


def exec_query():

    query = "SELECT Name from my_table WHERE Email = %s and Password = %s"

    cursor.execute(query, (mail,pwd))

    for data in cursor:
        for name in data:
            pass

    print_html(name)

exec_query()

