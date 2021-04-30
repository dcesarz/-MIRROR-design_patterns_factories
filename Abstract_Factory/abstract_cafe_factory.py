from abc import abstractmethod

from Abstract_Factory.factory_coffee import FactoryCoffee
from Abstract_Factory.factory_ice_cream import FactoryIceCream
from Abstract_Factory.factory_tea import FactoryTea
from singleton import Singleton


class IAbstractFactory(metaclass=Singleton):
    @staticmethod
    @abstractmethod
    def create_object(factory):
        pass


class AbstractCafeFactory(IAbstractFactory):
    @staticmethod
    def create_object(factory):
        try:
            if factory in ['coffee_espresso', 'coffee_cappucino',
                           'coffee_frappucino', 'coffee_latte',
                           'coffee_americano']:
                return FactoryCoffee.create_object(factory)
            if factory in ['tea_black', 'tea_red', 'tea_green',
                           'tea_white', 'tea_matcha']:
                return FactoryTea.create_object(factory)
            if factory in ['ice_cream_vanilla', 'ice_cream_chocolate',
                           'ice_cream_strawberry', 'ice_cream_coffee',
                           'ice_cream_mint']:
                return FactoryIceCream.create_object(factory)
            raise Exception('error: FACTORY NOT FOUND')
        except Exception as _e:
            print(_e)
        return None
