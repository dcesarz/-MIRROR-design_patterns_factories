from abc import ABCMeta, abstractmethod


class IProduct(metaclass=ABCMeta):
    @abstractmethod
    def operation(self) -> str:
        pass
