Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Car:
	x = 'My First Class'
	print(x)

	
My First Class
\
>>> Car
<class '__main__.Car'>
>>> Car()
<__main__.Car object at 0x01A5FC30>
>>> x
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> Car.x
'My First Class'
>>> class Emp:
	id = 1
	name = "Ram"
	age = 21

	
>>> Emp.id
1
>>> Emp.name
'Ram'
>>> Emp.age
21
>>> Emp.salary
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    Emp.salary
AttributeError: type object 'Emp' has no attribute 'salary'
>>> Emp.salary = 12000
>>> Emp.salary
12000
>>> obj_1 = Emp()
>>> obj_1
<__main__.Emp object at 0x03C72FF0>
>>> obj_1.id
1
>>> obj_1.name
'Ram'
>>> obj_1.salary
12000
>>> obj_2 = Emp()
>>> obj_2.id
1
>>> obj_2.id = 2
>>> Emp.id
1
>>> obj_1.id
1
>>> obj_2.id
2
>>> Emp.age = 25
>>> obj_1.age
25
>>> obj_2.age
25
>>> 
