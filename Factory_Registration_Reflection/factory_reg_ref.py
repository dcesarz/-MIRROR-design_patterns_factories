from singleton import Singleton


class FactoryRegistrationReflection(metaclass=Singleton):
    def __init__(self) -> None:
        self.registered_classes = {}

    def register(self, class_c):
        self.registered_classes[str(class_c)] = class_c

    @classmethod
    def create_object(cls, self, factory):
        imp = self.registered_classes[factory]()
        return imp.create_object()
