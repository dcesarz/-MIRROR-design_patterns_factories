from enum import Enum

from Simple_Factory.cafe_factory import CafeFactory as CafeFactory


class Menu(Enum):
    #   CODE NAMES -> CLASSES

    call = CafeFactory().create_object
    # coffee_espresso = CafeFactory().create_object
    # coffee_cappucino = CafeFactory().create_object
    # coffee_frappucino = CafeFactory().create_object
    # coffee_latte = CafeFactory().create_object
    # coffee_americano = CafeFactory().create_object
    #
    # tea_black = CafeFactory().create_object
    # tea_red = CafeFactory().create_object
    # tea_green = CafeFactory().create_object
    # tea_white = CafeFactory().create_object
    # tea_matcha = CafeFactory().create_object
    #
    # ice_cream_vanilla = CafeFactory().create_object
    # ice_cream_chocolate = CafeFactory().create_object
    # ice_cream_strawberry = CafeFactory().create_object
    # ice_cream_coffee = CafeFactory().create_object
    # ice_cream_mint = CafeFactory().create_object
    #
    # all_items_list = [coffee_espresso, coffee_cappucino, coffee_frappucino
    #     , coffee_latte, coffee_americano, tea_black, tea_red
    #     , tea_green, tea_white, tea_matcha, ice_cream_vanilla
    #     , ice_cream_chocolate, ice_cream_strawberry, ice_cream_coffee
    #     , ice_cream_mint]
