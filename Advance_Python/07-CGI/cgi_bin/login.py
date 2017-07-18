#!C:/Python36-32/python.exe

import cgi

form = cgi.FieldStorage()

mail = form.getvalue('u_mail')
pwd = form.getvalue('u_pwd')

# mail = "ram@gmail.com"
# pwd = "ramramramram"

message = ""

def success():
    print('Content-type:text/html\r\n\r\n')
    print("""
    <!DOCTYPE html>
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title></title>
        <link rel="stylesheet" href="/Python_New/login_form.css">
    </head>
    <body>
    <h1>Hello {}</h1>
    <h2>{}</h2>
    <h2>Password is {}</h2>
    </body>
    </html>
    """.format(mail,message, pwd))

def failure():
    print('Content-type:text/html\r\n\r\n')
    print("""
    <!DOCTYPE html>
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title></title>
        <link rel="stylesheet" href="/Python_New/login_form.css">
    </head>
    <body>
    <h1>{}</h1>
    <h2>Mail is {}</h2>
    <h2>Password is {}</h2>
    </body>
    </html>
    """.format(message,mail,pwd))

if mail == "ram@gmail.com":
    message = "Login Successfull"
    success()
else:
    message = "Login Failed"
    failure()