Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = "Hello this is python"
>>> "is" in a
True
>>> if "is" in a:
	print(True)

True
>>> a = "10"
>>> b = 10
>>> a == b
False
>>> 10 in a
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    10 in a
TypeError: 'in <string>' requires string as left operand, not int
>>> "10" in a
True
>>> a is b
False
>>> a is not b
True
>>> 
