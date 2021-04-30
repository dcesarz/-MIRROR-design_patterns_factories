from enum import Enum

import Factory_Registration_Reflection.coffee_implementations as coffee_implementations
import Factory_Registration_Reflection.ice_cream_implementations as ice_cream_implementations
import Factory_Registration_Reflection.tea_implementations as tea_implementations


class Menu(Enum):
    #   CODE NAMES -> CLASSES
    coffee_espresso = coffee_implementations.ConcreteCoffeeEspresso
    coffee_cappucino = coffee_implementations.ConcreteCoffeeCappucino
    coffee_frappucino = coffee_implementations.ConcreteCoffeeFrappucino
    coffee_latte = coffee_implementations.ConcreteCoffeeCappucino
    coffee_americano = coffee_implementations.ConcreteCoffeeAmericano

    tea_black = tea_implementations.ConcreteTeaBlack
    tea_red = tea_implementations.ConcreteTeaRed
    tea_green = tea_implementations.ConcreteTeaGreen
    tea_white = tea_implementations.ConcreteTeaWhite
    tea_matcha = tea_implementations.ConcreteTeaMatcha

    ice_cream_vanilla = ice_cream_implementations.ConcreteIceCreamVanilla
    ice_cream_chocolate = ice_cream_implementations.ConcreteIceCreamChocolate
    ice_cream_strawberry = ice_cream_implementations.ConcreteIceCreamStrawberry
    ice_cream_coffee = ice_cream_implementations.ConcreteIceCreamCoffee
    ice_cream_mint = ice_cream_implementations.ConcreteIceCreamMint

    all_items_list = [coffee_espresso, coffee_cappucino, coffee_frappucino
        , coffee_latte, coffee_americano, tea_black, tea_red
        , tea_green, tea_white, tea_matcha, ice_cream_vanilla
        , ice_cream_chocolate, ice_cream_strawberry, ice_cream_coffee
        , ice_cream_mint]
