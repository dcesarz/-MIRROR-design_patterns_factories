from Abstract_Factory.menu import Menu as menuAbstract
from Factory_Method.menu import Menu as menuFm
from Factory_Registration.factory_reg import FactoryRegistration
from Factory_Registration.menu import Menu as menuRegi
from Factory_Registration_Reflection.factory_reg_ref import FactoryRegistrationReflection
from Factory_Registration_Reflection.menu import Menu as menuRegiRef
from Simple_Factory.menu import Menu as menuSimple

menus_reg = [menuRegi.all_items_list, menuRegiRef.all_items_list]

fr = FactoryRegistration().registered_classes
frr = FactoryRegistrationReflection().registered_classes

all_items_list = ['coffee_espresso', 'coffee_cappucino', 'coffee_frappucino'
    , 'coffee_latte', 'coffee_americano', 'tea_black', 'tea_red'
    , 'tea_green', 'tea_white', 'tea_matcha', 'ice_cream_vanilla'
    , 'ice_cream_chocolate', 'ice_cream_strawberry', 'ice_cream_coffee'
    , 'ice_cream_mint']


def register():
    for item in menus_reg[0].value:
        FactoryRegistration().register(item[0], item[1])


def register_with_reflection():
    for item in menus_reg[1].value:
        FactoryRegistrationReflection().register(item)


def exec_abstract(amount):
    length = len(all_items_list)
    for i in range(amount):
        for l in range(length):
            menuAbstract.call(all_items_list[l])


def exec_fm(amount):
    length = len(all_items_list)
    for i in range(amount):
        for l in range(length):
            inst = menuFm.all_items_list.value[l]()
            inst.some_operation()


def exec_simple(amount):
    length = len(all_items_list)
    for i in range(amount):
        for l in range(length):
            menuSimple.call(all_items_list[l])


def exec_fr(amount):
    fr = FactoryRegistration().registered_classes
    for i in range(amount):
        for fr_item in fr:
            FactoryRegistration.create_object(FactoryRegistration(), fr_item)


def exec_frr(amount):
    frr = FactoryRegistrationReflection().registered_classes
    for i in range(amount):
        for frr_item in frr:
            FactoryRegistrationReflection.create_object(FactoryRegistrationReflection(), frr_item)


def exec_all():
    exec_abstract(1)
    exec_fm(1)
    exec_simple(1)
    exec_fr(1)
    exec_frr(1)


register()
register_with_reflection()
exec_all()
