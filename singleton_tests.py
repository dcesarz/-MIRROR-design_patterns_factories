#   just a quick test to verify if all factories are singletons and work as such.

import numpy as np

import Factory_Method.concrete_creator_coffee
import Factory_Method.concrete_creator_ice_cream
import Factory_Method.concrete_creator_tea
from Abstract_Factory.abstract_cafe_factory import AbstractCafeFactory
from Abstract_Factory.factory_coffee import FactoryCoffee
from Abstract_Factory.factory_ice_cream import FactoryIceCream
from Abstract_Factory.factory_tea import FactoryTea
from Factory_Method.creator_cafe import CafeCreator
from Factory_Registration.factory_reg import FactoryRegistration
from Factory_Registration_Reflection.factory_reg_ref import FactoryRegistrationReflection
from Simple_Factory.cafe_factory import CafeFactory

singleton_list = [AbstractCafeFactory,
                  FactoryCoffee,
                  FactoryTea,
                  FactoryIceCream,
                  CafeCreator,
                  Factory_Method.concrete_creator_coffee.ConcreteCreatorCoffeeEspresso,
                  Factory_Method.concrete_creator_coffee.ConcreteCreatorCoffeeCappucino,
                  Factory_Method.concrete_creator_coffee.ConcreteCreatorCoffeeFrappucino,
                  Factory_Method.concrete_creator_coffee.ConcreteCreatorCoffeeLatte,
                  Factory_Method.concrete_creator_coffee.ConcreteCreatorCoffeeAmericano,
                  Factory_Method.concrete_creator_tea.ConcreteCreatorTeaBlack,
                  Factory_Method.concrete_creator_tea.ConcreteCreatorTeaRed,
                  Factory_Method.concrete_creator_tea.ConcreteCreatorTeaGreen,
                  Factory_Method.concrete_creator_tea.ConcreteCreatorTeaWhite,
                  Factory_Method.concrete_creator_tea.ConcreteCreatorTeaMatcha,
                  Factory_Method.concrete_creator_ice_cream.ConcreteCreatorIceCreamVanilla,
                  Factory_Method.concrete_creator_ice_cream.ConcreteCreatorIceCreamChocolate,
                  Factory_Method.concrete_creator_ice_cream.ConcreteCreatorIceCreamStrawberry,
                  Factory_Method.concrete_creator_ice_cream.ConcreteCreatorIceCreamCoffee,
                  Factory_Method.concrete_creator_ice_cream.ConcreteCreatorIceCreamMint,
                  CafeFactory,
                  FactoryRegistration,
                  FactoryRegistrationReflection]


def appendtwo(item, l2, index):
    l2[index][0] = item()
    l2[index][1] = item()
    return l2


def get_singleton_comp_list():
    singleton_list_comp = np.arange(len(singleton_list) * 2).reshape(len(singleton_list), 2)
    singleton_list_comp = np.ndarray.tolist(singleton_list_comp)
    for i in range(len(singleton_list)):
        singleton_list_comp = appendtwo(singleton_list[i], singleton_list_comp, i)
    return singleton_list_comp


comp_list = get_singleton_comp_list()

for i in comp_list:
    if i[0] == i[1]:
        print("Equals, all good")
    else:
        print("Not equal.")
