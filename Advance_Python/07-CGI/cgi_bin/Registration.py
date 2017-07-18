#!C:/Python36-32/python.exe

import cgi

form = cgi.FieldStorage()

name = form.getvalue('u_name')
mail = form.getvalue('u_mail')
pwd = form.getvalue('u_pwd')
dob = form.getvalue('u_dob')

if form.getvalue('city'):
    city = form.getvalue('city')
else:
    city = 'undefined'

gender = form.getvalue('gender')
hobby = form.getvalue('hobby')

print('Content-type:text/html\r\n\r\n')

print("""
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
<h1>Hello {}</h1>
<h2>Email is {} </h2>
<h2>Password is {}</h2>
<h2>Born Date is {}</h2>
<h2>City {}</h2>
<h2>Gender {}</h2>
<h2>Hobby {}</h2>
</body>
</html>
""".format(name, mail, pwd, dob, city, gender, hobby))