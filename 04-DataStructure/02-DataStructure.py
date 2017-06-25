Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [1,2,3,4,5,6]
>>> a.append('Hi')
>>> a
[1, 2, 3, 4, 5, 6, 'Hi']
>>> a.append('Python')
>>> a
[1, 2, 3, 4, 5, 6, 'Hi', 'Python']
>>> a.append('This','is','awesome')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.append('This','is','awesome')
TypeError: append() takes exactly one argument (3 given)
>>> a.append(['This','is','awesome'])
>>> a
[1, 2, 3, 4, 5, 6, 'Hi', 'Python', ['This', 'is', 'awesome']]
>>> a.append(['Python','programming'])
>>> a
[1, 2, 3, 4, 5, 6, 'Hi', 'Python', ['This', 'is', 'awesome'], ['Python', 'programming']]
>>> a[-1]
['Python', 'programming']
>>> a[-1][1]
'programming'
>>> a.pop()
['Python', 'programming']
>>> a
[1, 2, 3, 4, 5, 6, 'Hi', 'Python', ['This', 'is', 'awesome']]
>>> a.pop(2)
3
>>> a
[1, 2, 4, 5, 6, 'Hi', 'Python', ['This', 'is', 'awesome']]
>>> a.insert(0,'Hello')
>>> a
['Hello', 1, 2, 4, 5, 6, 'Hi', 'Python', ['This', 'is', 'awesome']]
>>> a.remove(0)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.remove(0)
ValueError: list.remove(x): x not in list
>>> a.remove('Hello')
>>> a
[1, 2, 4, 5, 6, 'Hi', 'Python', ['This', 'is', 'awesome']]
>>> a.count('Python')
1
>>> len(a)
8
>>> del(a[2])
>>> a
[1, 2, 5, 6, 'Hi', 'Python', ['This', 'is', 'awesome']]
>>> x = "Hello world"
>>> del (x[0])
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    del (x[0])
TypeError: 'str' object doesn't support item deletion
>>> x[0]
'H'
>>> a
[1, 2, 5, 6, 'Hi', 'Python', ['This', 'is', 'awesome']]
>>> a = [1,3,6,2,67,23,4,7,9,3,4,23,56]
>>> sorted(a)
[1, 2, 3, 3, 4, 4, 6, 7, 9, 23, 23, 56, 67]
>>> sorted(a,reverse=True)
[67, 56, 23, 23, 9, 7, 6, 4, 4, 3, 3, 2, 1]
>>> a = ['Ram','Akash','Rohan','Amit','Zayn','Chotu','Pooja','Ravi','Yogi']
>>> sorted(a)
['Akash', 'Amit', 'Chotu', 'Pooja', 'Ram', 'Ravi', 'Rohan', 'Yogi', 'Zayn']
>>> help()

Welcome to Python 3.6's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/3.6/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> list
Help on class list in module builtins:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.n
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |  
 |  __rmul__(self, value, /)
 |      Return self*value.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |  
 |  append(...)
 |      L.append(object) -> None -- append object to end
 |  
 |  clear(...)
 |      L.clear() -> None -- remove all items from L
 |  
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

help> tuples
No Python documentation found for 'tuples'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> tuple
Help on class tuple in module builtins:

class tuple(object)
 |  tuple() -> empty tuple
 |  tuple(iterable) -> tuple initialized from iterable's items
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.n
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmul__(self, value, /)
 |      Return self*value.
 |  
 |  count(...)
 |      T.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.

help> 
quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> a= [1, 2, 5, 6, 'Hi', 'Python','This', 'is', 'awesome']
>>> a.extend("Python is super easy")
>>> a
[1, 2, 5, 6, 'Hi', 'Python', 'This', 'is', 'awesome', 'P', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 's', 'u', 'p', 'e', 'r', ' ', 'e', 'a', 's', 'y']
>>> a.pop()
'y'
>>> a= [1, 2, 5, 6, 'Hi', 'Python','This', 'is', 'awesome']
>>> a.extend(["Python is super easy"])
>>> a
[1, 2, 5, 6, 'Hi', 'Python', 'This', 'is', 'awesome', 'Python is super easy']
>>> a.extend(["Python","is","super","easy"])
>>> a
[1, 2, 5, 6, 'Hi', 'Python', 'This', 'is', 'awesome', 'Python is super easy', 'Python', 'is', 'super', 'easy']
>>> 
