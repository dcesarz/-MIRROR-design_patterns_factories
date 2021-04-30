from enum import Enum

from Abstract_Factory.abstract_cafe_factory import AbstractCafeFactory


class Menu(Enum):
    call = AbstractCafeFactory().create_object
