from Abstract_Factory.product_interface import IProduct
from config import enable_prints as e
from singleton import Singleton


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


class FactoryCoffee(metaclass=Singleton):
    @staticmethod
    def create_object(prop):
        try:
            if prop == 'coffee_espresso':
                return ConcreteCoffeeEspresso()
            if prop == 'coffee_cappucino':
                return ConcreteCoffeeCappucino()
            if prop == 'coffee_frappucino':
                return ConcreteCoffeeFrappucino()
            if prop == 'coffee_latte':
                return ConcreteCoffeeLatte()
            if prop == 'coffee_americano':
                return ConcreteCoffeeAmericano()
            raise Exception('error: CLASS NOT FOUND')
        except Exception as _e:
            print(_e)
        return None
