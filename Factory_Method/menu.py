from enum import Enum

from Factory_Method import concrete_creator_coffee
from Factory_Method import concrete_creator_ice_cream
from Factory_Method import concrete_creator_tea


class Menu(Enum):
    #   CODE NAMES -> CLASSES

    coffee_espresso = concrete_creator_coffee.ConcreteCreatorCoffeeEspresso
    coffee_cappucino = concrete_creator_coffee.ConcreteCreatorCoffeeCappucino
    coffee_frappucino = concrete_creator_coffee.ConcreteCreatorCoffeeFrappucino
    coffee_latte = concrete_creator_coffee.ConcreteCreatorCoffeeLatte
    coffee_americano = concrete_creator_coffee.ConcreteCreatorCoffeeAmericano

    tea_black = concrete_creator_tea.ConcreteCreatorTeaBlack
    tea_red = concrete_creator_tea.ConcreteCreatorTeaRed
    tea_green = concrete_creator_tea.ConcreteCreatorTeaGreen
    tea_white = concrete_creator_tea.ConcreteCreatorTeaWhite
    tea_matcha = concrete_creator_tea.ConcreteCreatorTeaMatcha

    ice_cream_vanilla = concrete_creator_ice_cream.ConcreteCreatorIceCreamVanilla
    ice_cream_chocolate = concrete_creator_ice_cream.ConcreteCreatorIceCreamChocolate
    ice_cream_strawberry = concrete_creator_ice_cream.ConcreteCreatorIceCreamStrawberry
    ice_cream_coffee = concrete_creator_ice_cream.ConcreteCreatorIceCreamCoffee
    ice_cream_mint = concrete_creator_ice_cream.ConcreteCreatorIceCreamMint

    all_items_list = [coffee_espresso, coffee_cappucino, coffee_frappucino,
                      coffee_latte, coffee_americano, tea_black, tea_red,
                      tea_green, tea_white, tea_matcha, ice_cream_vanilla,
                      ice_cream_chocolate, ice_cream_strawberry, ice_cream_coffee,
                      ice_cream_mint]
