#!C:/Python36-32/python.exe

import cgi

form = cgi.FieldStorage()

f_num = form.getvalue('f_num')
s_num = form.getvalue('s_num')

result = int(f_num) + int(s_num)

print('Content-type:text/html\r\n\r\n')

print("""
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
<h1>Hello World</h1>
<h2>Sum is {}</h2>
</body>
</html>
""".format(result))