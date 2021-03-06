from abc import ABCMeta, abstractmethod


class IProduct(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def create_object():
        pass
