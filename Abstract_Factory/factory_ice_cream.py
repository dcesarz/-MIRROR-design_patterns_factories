from Abstract_Factory.product_interface import IProduct
from config import enable_prints as e
from singleton import Singleton


class ConcreteIceCreamVanilla(IProduct):
    def __init__(self):
        self.name = str(self.__class__)
        if e: print(self.name)

    def create_object(self):
        return self


class ConcreteIceCreamChocolate(IProduct):
    def __init__(self):
        self.name = str(self.__class__)
        if e: print(self.name)

    def create_object(self):
        return self


class ConcreteIceCreamStrawberry(IProduct):
    def __init__(self):
        self.name = str(self.__class__)
        if e: print(self.name)

    def create_object(self):
        return self


class ConcreteIceCreamCoffee(IProduct):
    def __init__(self):
        self.name = str(self.__class__)
        if e: print(self.name)

    def create_object(self):
        return self


class ConcreteIceCreamMint(IProduct):
    def __init__(self):
        self.name = str(self.__class__)
        if e: print(self.name)

    def create_object(self):
        return self


class FactoryIceCream(metaclass=Singleton):
    @staticmethod
    def create_object(prop):
        try:
            if prop == 'ice_cream_vanilla':
                return ConcreteIceCreamVanilla()
            if prop == 'ice_cream_chocolate':
                return ConcreteIceCreamChocolate()
            if prop == 'ice_cream_strawberry':
                return ConcreteIceCreamStrawberry()
            if prop == 'ice_cream_coffee':
                return ConcreteIceCreamCoffee()
            if prop == 'ice_cream_mint':
                return ConcreteIceCreamMint()
            raise Exception('error: CLASS NOT FOUND')
        except Exception as _e:
            print(_e)
        return None
