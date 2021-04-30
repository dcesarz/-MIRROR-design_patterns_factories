from __future__ import annotations

from Factory_Method.creator_cafe import CafeCreator
from Factory_Method.product_interface import IProduct


class ConcreteCreatorTeaBlack(CafeCreator):
    def factory_method(self) -> IProduct:
        return ConcreteTeaBlack()


class ConcreteCreatorTeaRed(CafeCreator):
    def factory_method(self) -> IProduct:
        return ConcreteTeaRed()


class ConcreteCreatorTeaGreen(CafeCreator):
    def factory_method(self) -> IProduct:
        return ConcreteTeaGreen()


class ConcreteCreatorTeaWhite(CafeCreator):
    def factory_method(self) -> IProduct:
        return ConcreteTeaWhite()


class ConcreteCreatorTeaMatcha(CafeCreator):
    def factory_method(self) -> IProduct:
        return ConcreteTeaMatcha()


class ConcreteTeaBlack(IProduct):
    def operation(self) -> str:
        return str(self.__class__)


class ConcreteTeaRed(IProduct):
    def operation(self) -> str:
        return str(self.__class__)


class ConcreteTeaGreen(IProduct):
    def operation(self) -> str:
        return str(self.__class__)


class ConcreteTeaWhite(IProduct):
    def operation(self) -> str:
        return str(self.__class__)


class ConcreteTeaMatcha(IProduct):
    def operation(self) -> str:
        return str(self.__class__)
