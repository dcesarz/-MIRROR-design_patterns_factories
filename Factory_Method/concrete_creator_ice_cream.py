from __future__ import annotations

from Factory_Method.creator_cafe import CafeCreator
from Factory_Method.product_interface import IProduct


class ConcreteCreatorIceCreamVanilla(CafeCreator):
    def factory_method(self) -> IProduct:
        return ConcreteIceCreamVanilla()


class ConcreteCreatorIceCreamChocolate(CafeCreator):
    def factory_method(self) -> IProduct:
        return ConcreteIceCreamChocolate()


class ConcreteCreatorIceCreamStrawberry(CafeCreator):
    def factory_method(self) -> IProduct:
        return ConcreteIceCreamStrawberry()


class ConcreteCreatorIceCreamCoffee(CafeCreator):
    def factory_method(self) -> IProduct:
        return ConcreteIceCreamCoffee()


class ConcreteCreatorIceCreamMint(CafeCreator):
    def factory_method(self) -> IProduct:
        return ConcreteIceCreamMint()


class ConcreteIceCreamVanilla(IProduct):
    def operation(self) -> str:
        return str(self.__class__)


class ConcreteIceCreamChocolate(IProduct):
    def operation(self) -> str:
        return str(self.__class__)


class ConcreteIceCreamStrawberry(IProduct):
    def operation(self) -> str:
        return str(self.__class__)


class ConcreteIceCreamCoffee(IProduct):
    def operation(self) -> str:
        return str(self.__class__)


class ConcreteIceCreamMint(IProduct):
    def operation(self) -> str:
        return str(self.__class__)
