class Emp:

    def __init__(self):
        self._x = ""
        self.__y = ""

    def __get__(self):
        self.__y = "Value Changed"
        return self.__y

    def __set__(self):
        self._x = "Value changed again"
        return self._x

    def show_val(self):
        print(self._x, self.__y)



class User(Emp):

    def show_val(self):
        print(super().__set__())
        print(super().__get__())


# obj = Emp("Inside X", "Inside Y")
# print(obj._x)
# obj.show_val()
# print(obj.__get__())
# print(obj.__set__())

obj = User()
obj.show_val()