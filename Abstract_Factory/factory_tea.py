from Abstract_Factory.product_interface import IProduct
from config import enable_prints as e
from singleton import Singleton


class ConcreteTeaBlack(IProduct):
    def __init__(self):
        self.name = str(self.__class__)
        if e: print(self.name)

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


class FactoryTea(metaclass=Singleton):
    @staticmethod
    def create_object(prop):
        try:
            if prop == 'tea_black':
                return ConcreteTeaBlack()
            if prop == 'tea_red':
                return ConcreteTeaRed()
            if prop == 'tea_green':
                return ConcreteTeaGreen()
            if prop == 'tea_white':
                return ConcreteTeaWhite()
            if prop == 'tea_matcha':
                return ConcreteTeaMatcha()
            raise Exception('error: CLASS NOT FOUND')
        except Exception as _e:
            print(_e)
        return None
