Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = "Hello Python"
>>> a.split(" ")
['Hello', 'Python']
>>> a = [1,2,3,4,5,6,7]
>>> for i in a:
	print(i)

1
2
3
4
5
6
7
>>> for i in a:
	print(i,end="")

1234567
>>> a = [1,2,3,4,5,6,7]
>>> a = ("red","green","blue")
>>> a
('red', 'green', 'blue')
>>> a = {"id":101,"name":"Ram","Age":20}
>>> a
{'id': 101, 'name': 'Ram', 'Age': 20}
>>> a.id
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.id
AttributeError: 'dict' object has no attribute 'id'
>>> a[id]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a[id]
KeyError: <built-in function id>
>>> for i in a:
	print(i)

id
name
Age
>>> for i in a.items():
	print(i)

('id', 101)
('name', 'Ram')
('Age', 20)
>>> for i in a.value():
	print(i)

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    for i in a.value():
AttributeError: 'dict' object has no attribute 'value'
>>> for i in a.values():
	print(i)

101
Ram
20
>>> a["name"] = "Shyam"
>>> a
{'id': 101, 'name': 'Shyam', 'Age': 20}
>>> a["sal"] = 20000
>>> a
{'id': 101, 'name': 'Shyam', 'Age': 20, 'sal': 20000}
>>> a.keys()
dict_keys(['id', 'name', 'Age', 'sal'])
>>> a.values()
dict_values([101, 'Shyam', 20, 20000])
>>> a.items()
dict_items([('id', 101), ('name', 'Shyam'), ('Age', 20), ('sal', 20000)])
>>> a["address"] = ["11-C, Rohini East","Noida Sector-62"]
>>> a
{'id': 101, 'name': 'Shyam', 'Age': 20, 'sal': 20000, 'address': ['11-C, Rohini East', 'Noida Sector-62']}
>>> for i in a.values():
	print(i)

101
Shyam
20
20000
['11-C, Rohini East', 'Noida Sector-62']
>>> a[1]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a[1]
KeyError: 1
>>> a[0]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a[0]
KeyError: 0
>>> a[name]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a[name]
NameError: name 'name' is not defined
>>> a["name"]
'Shyam'
>>> a["address"]
['11-C, Rohini East', 'Noida Sector-62']
>>> a["address"][1]
'Noida Sector-62'
>>> import pygame
>>> 
