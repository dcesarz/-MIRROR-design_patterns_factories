from Simple_Factory.product_interface import IProduct
from config import enable_prints as e


class ConcreteTeaBlack(IProduct):
    def __init__(self):
        self.name = str(self.__class__)
        if e:
            print(self.name)

    def create_object(self):
        return self


class ConcreteTeaRed(IProduct):
    def __init__(self):
        self.name = str(self.__class__)
        if e: print(self.name)

    def create_object(self):
        return self


class ConcreteTeaGreen(IProduct):
    def __init__(self):
        self.name = str(self.__class__)
        if e: print(self.name)

    def create_object(self):
        return self


class ConcreteTeaWhite(IProduct):
    def __init__(self):
        self.name = str(self.__class__)
        if e: print(self.name)

    def create_object(self):
        return self


class ConcreteTeaMatcha(IProduct):
    def __init__(self):
        self.name = str(self.__class__)
        if e: print(self.name)

    def create_object(self):
        return self
