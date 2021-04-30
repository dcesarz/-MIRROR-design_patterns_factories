import Simple_Factory.coffee_implementations as coffee_implementations
import Simple_Factory.ice_cream_implementations as ice_cream_implementations
import Simple_Factory.tea_implementations as tea_implementations
from singleton import Singleton


class CafeFactory(metaclass=Singleton):
    @classmethod
    def create_object(cls, factory):
        try:
            if factory == 'coffee_espresso':
                imp = coffee_implementations.ConcreteCoffeeEspresso()
                return imp.create_object()
            if factory == 'coffee_cappucino':
                imp = coffee_implementations.ConcreteCoffeeCappucino()
                return imp.create_object()
            if factory == 'coffee_frappucino':
                imp = coffee_implementations.ConcreteCoffeeFrappucino()
                return imp.create_object()
            if factory == 'coffee_latte':
                imp = coffee_implementations.ConcreteCoffeeLatte()
                return imp.create_object()
            if factory == 'coffee_americano':
                imp = coffee_implementations.ConcreteCoffeeAmericano()
                return imp.create_object()
            if factory == 'tea_black':
                imp = tea_implementations.ConcreteTeaBlack()
                return imp.create_object()
            if factory == 'tea_red':
                imp = tea_implementations.ConcreteTeaRed()
                return imp.create_object()
            if factory == 'tea_green':
                imp = tea_implementations.ConcreteTeaGreen()
                return imp.create_object()
            if factory == 'tea_white':
                imp = tea_implementations.ConcreteTeaWhite()
                return imp.create_object()
            if factory == 'tea_matcha':
                imp = tea_implementations.ConcreteTeaMatcha()
                return imp.create_object()
            if factory == 'ice_cream_vanilla':
                imp = ice_cream_implementations.ConcreteIceCreamVanilla()
                return imp.create_object()
            if factory == 'ice_cream_chocolate':
                imp = ice_cream_implementations.ConcreteIceCreamChocolate()
                return imp.create_object()
            if factory == 'ice_cream_strawberry':
                imp = ice_cream_implementations.ConcreteIceCreamStrawberry()
                return imp.create_object()
            if factory == 'ice_cream_coffee':
                imp = ice_cream_implementations.ConcreteIceCreamCoffee()
                return imp.create_object()
            if factory == 'ice_cream_mint':
                imp = ice_cream_implementations.ConcreteIceCreamMint()
                return imp.create_object()
            raise Exception('error: FACTORY NOT FOUND')
        except Exception as _e:
            print(_e)
        return None
