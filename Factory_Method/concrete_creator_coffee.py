from __future__ import annotations

from Factory_Method.creator_cafe import CafeCreator
from Factory_Method.product_interface import IProduct


class ConcreteCreatorCoffeeEspresso(CafeCreator):
    def factory_method(self) -> IProduct:
        return ConcreteCoffeeEspresso()


class ConcreteCreatorCoffeeCappucino(CafeCreator):
    def factory_method(self) -> IProduct:
        return ConcreteCoffeeCappucino()


class ConcreteCreatorCoffeeFrappucino(CafeCreator):
    def factory_method(self) -> IProduct:
        return ConcreteCoffeeFrappucino()


class ConcreteCreatorCoffeeLatte(CafeCreator):
    def factory_method(self) -> IProduct:
        return ConcreteCoffeeLatte()


class ConcreteCreatorCoffeeAmericano(CafeCreator):
    def factory_method(self) -> IProduct:
        return ConcreteCoffeeAmericano()


class ConcreteCoffeeEspresso(IProduct):
    def operation(self) -> str:
        return str(self.__class__)


class ConcreteCoffeeCappucino(IProduct):
    def operation(self) -> str:
        return str(self.__class__)


class ConcreteCoffeeFrappucino(IProduct):
    def operation(self) -> str:
        return str(self.__class__)


class ConcreteCoffeeLatte(IProduct):
    def operation(self) -> str:
        return str(self.__class__)


class ConcreteCoffeeAmericano(IProduct):
    def operation(self) -> str:
        return str(self.__class__)
