#!C:/Python36-32/python.exe

import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='fb_register', autocommit=True)

cursor = connection.cursor()

# cursor.execute("CREATE TABLE products ( id INT(255) NOT NULL , Name VARCHAR(255) NOT NULL ,"
#                " Price INT(255) NOT NULL , Details VARCHAR(255) NOT NULL , PRIMARY KEY (id));")

cursor.execute("INSERT INTO products (id,Name,Price,Details) VALUES ('1','Samsung','23000','Galaxy S8') ")