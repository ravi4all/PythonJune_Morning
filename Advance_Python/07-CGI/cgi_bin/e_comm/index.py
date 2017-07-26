#!C:/Python36-32/python.exe

import pymysql
import cgi

connection = pymysql.connect(host='localhost', port = 3306, user='root', passwd='',
                             db = 'e_commerce', autocommit = True)

cursor = connection.cursor()

def print_html(data):
    print("""
    <!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>

<h1>Data {} </h1>

</body>
</html>
    """.format(data))

def success():

    query = "SELECT * FROM products "
    cursor.execute(query)

    for data in cursor:
        img = data[4]

    # fh = open("imageToSave.png", "wb")
    # fh.write(str.decode('base64'))
    # fh.close()

    #print_html(data)

success()