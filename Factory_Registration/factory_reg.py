from singleton import Singleton


class FactoryRegistration(metaclass=Singleton):
    def __init__(self) -> None:
        self.registered_classes = {}

    def register(self, class_name, class_init):
        self.registered_classes[class_name] = class_init

    @classmethod
    def create_object(cls, self, factory):
        imp = self.registered_classes[factory]()
        return imp.create_object()
