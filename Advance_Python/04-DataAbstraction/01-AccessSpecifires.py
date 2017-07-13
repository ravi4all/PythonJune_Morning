class Emp:

    _x = "Inside X"
    __y = "Inside Y"

    def __get__(self):
        self.__y = "Value Changed"
        return self.__y

    def __set__(self):
        self._x = "Value changed again"
        return self._x

obj = Emp()
print(obj._x)

print(obj.__get__())
print(obj.__set__())
