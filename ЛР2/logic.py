class StandardLogic(object):
    def __init__(self, a=1, b=2):
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

    def calculate(self, sign: str):
        operations = {'+': self.sum,
                      '-': self.subtract,
                      '/': self.divide,
                      '*': self.multiply}
        if sign in operations:
            return operations[sign]()
        raise ValueError

    def sum(self):
        return self.__a + self.__b

    def subtract(self):
        return self.__a - self.__b

    def divide(self):
        return self.__a / self.__b

    def multiply(self):
        return self.__a * self.__b


class ExtendedLogic(StandardLogic):
    def get_miles(self):
        return self.a * 0.62137
