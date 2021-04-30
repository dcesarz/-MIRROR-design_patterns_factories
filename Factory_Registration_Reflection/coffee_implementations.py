from Simple_Factory.product_interface import IProduct
from config import enable_prints as e


class ConcreteCoffeeEspresso(IProduct):
    def __init__(self):
        self.name = str(self.__class__)
        if e: print(self.name)

    def create_object(self):
        return self


class ConcreteCoffeeCappucino(IProduct):
    def __init__(self):
        self.name = str(self.__class__)
        if e: print(self.name)

    def create_object(self):
        return self


class ConcreteCoffeeFrappucino(IProduct):
    def __init__(self):
        self.name = str(self.__class__)
        if e: print(self.name)

    def create_object(self):
        return self


class ConcreteCoffeeLatte(IProduct):
    def __init__(self):
        self.name = str(self.__class__)
        if e: print(self.name)

    def create_object(self):
        return self


class ConcreteCoffeeAmericano(IProduct):
    def __init__(self):
        self.name = str(self.__class__)
        if e: print(self.name)

    def create_object(self):
        return self
