#!C:/Python36-32/python.exe

a = 10
b = 20
c = a + b

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
<img src="http://media2.intoday.in/indiatoday/images/stories/647_010517091159.jpg" alt="image"/>
</body>
</html>
""".format(c))