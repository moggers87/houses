from house.items import PhysicalObject


class Person(PhysicalObject):
    def __init__(self, name):
        self.name = name
