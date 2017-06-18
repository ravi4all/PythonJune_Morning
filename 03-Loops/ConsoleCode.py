Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = "This is python programming"
>>> print("This isn't python")
This isn't python
>>> print("This isn't "python"")\
	    
SyntaxError: invalid syntax
>>> print("This isn't "python"")
SyntaxError: invalid syntax
>>> 
>>> print('This isn't "python"')
      
SyntaxError: invalid syntax
>>> print('This isn\'t "python"')
This isn't "python"
>>> print("""This isn\'t "python"""")
      
SyntaxError: EOL while scanning string literal
>>> print("""This isn\'t 'python'""")
This isn't 'python'
>>> a = [1,2,3,"Hello",10.5,True,120.00000]
>>> b = (1,2,3,"Hello",10.5,True,120.00000)
>>> b
(1, 2, 3, 'Hello', 10.5, True, 120.0)
>>> a[0] = "Python"
>>> a
['Python', 2, 3, 'Hello', 10.5, True, 120.0]
>>> b[0] = "Python"
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    b[0] = "Python"
TypeError: 'tuple' object does not support item assignment
>>> a = "10"
>>> b = "20"
>>> a+b
'1020'
>>> int(a) + int(b)
30
>>> import random
>>> pygame.init()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    pygame.init()
NameError: name 'pygame' is not defined
>>> import pygame
>>> 
>>> pygame.init()
(6, 0)
>>> a = ["stone","paper","scissor"]
>>> random.choice(a)
'stone'
>>> random.choice(a)
'stone'
>>> random.choice(a)
'stone'
>>> a = "Ram"
>>> b = 20
>>> print("Name is",a "and age is",b)
SyntaxError: invalid syntax
>>> print("Name is",a, "and age is",b)
Name is Ram and age is 20
>>> print("Name is {} and age is {}".format(a,b))
Name is Ram and age is 20
>>> a = [1,2,3,4,5,6,7,8,9,10]
>>> for i in a:
	print(2*i)

2
4
6
8
10
12
14
16
18
20
>>> a = 20
>>> while a > 0:
	print(a)
	a -= 1

	
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
>>> a = True
>>> a,b = 10,12
>>> a
10
>>> b
12
>>> a = b
>>> b = a
>>> a
12
>>> b
12
>>> a,b = 10,12
>>> a,b = b,a
>>> a
12
>>> b
10
>>> for i in range(0,10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(1,11):
	print(i)

	
1
2
3
4
5
6
7
8
9
10
>>> for i in range(1,11):
	print(i*2)

	
2
4
6
8
10
12
14
16
18
20
>>> for i in range(1,100,2):
	print(i)

	
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
61
63
65
67
69
71
73
75
77
79
81
83
85
87
89
91
93
95
97
99
>>> for i in range(3,100,3):
	print(i)

	
3
6
9
12
15
18
21
24
27
30
33
36
39
42
45
48
51
54
57
60
63
66
69
72
75
78
81
84
87
90
93
96
99
>>> a = [x for x in range(1,100,3)]
>>> a
[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97]
>>> a = [i for i in range(1,50) if i%2==0]
>>> a
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> 
