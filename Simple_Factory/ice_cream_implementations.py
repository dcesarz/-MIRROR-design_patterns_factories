from Simple_Factory.product_interface import IProduct
from config import enable_prints as e


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
