from __future__ import annotations

from abc import abstractmethod

from config import enable_prints as e
from singleton import Singleton


class CafeCreator(metaclass=Singleton):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        #   basic operation

        product = self.factory_method()
        result = f"Creator: Operation : {product.operation()}"

        if e:
            print(result)

        return result
