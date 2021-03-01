class StandardLogic(object):
    def __init__(self, a = 1, b = 2):
        self.__a = a
        self.__b = b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    def sum(self):
        return self.__a + self.__b

    def substract(self):
        return self.__a - self.__b

    def divide(self):
        return self.__a / self.__b

    def multiply(self):
        return self.__a * self.__b
