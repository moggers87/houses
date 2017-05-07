import inspect
import logging

from houses import house, items, person

log = logging.get_logger(__name__)


def get_classes(module, baseclass):
    def is_subclass(obj):
        return inspect.isclass(obj) and issubclass(obj, baseclass)

    return inspect.getmembers(module, is_subclass)


HOUSE_TYPES = {"house.{}".format(name): cls for name, cls in get_classes(house, house.House)}
ITEM_TYPES = {"item.{}".format(name): cls for name, cls in get_classes(items, items.PhysicalObject)}
PERSON_TYPES = {"person.{}".format(name): cls for name, cls in get_classes(person, person.Person)}


class Simulator(object):
    def __init__(self, houses):
        self.houses = houses

    @classmethod
    def from_dict(cls, data):
        """
        Create a simulation from data

        Example data:
        [
            {
                "type": "house.House",
                "name": "Bob's house",
                "plotX": 100,
                "plotY": 120,
                "residents": [
                    {
                        "type": "person.Person",
                        "name": "Bob",
                        "positionX": 45,
                        "positionY": 34,
                    },
                    ...
                ],
                "items": [
                    {
                        "type": "item.Wall",
                        "positionX": 46,
                        "positionY": 34,
                    },
                    ...
                ],
            },
            ...
        ]
        """

        houses = []

        for house_data in data:
            house_type = house_data["type"]
            name = house_data["name"]
            plot_size = (house_data["plotX"], house_data["plotY"])

            house = HOUSE_TYPES[house_type](name=name, plot_size=plot_size)

            for item_data in house_data.get("items", []):
                item_type = item_data["type"]
                position = (item_data["positionX"], item_data["positionY"])

                item = ITEM_TYPES[item_type]()
                house.objects.add(position, item)

            for person_data in house_data.get("residents", []):
                person_type = person_data["type"]
                name = person_data["name"]
                position = (person_data["positionX"], person_data["positionY"])

                person = PERSON_TYPES[person_type](name=name)
                house.objects.add(position, person)

            houses.append(house)

        return cls(houses)
