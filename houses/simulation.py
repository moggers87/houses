##
# Copyright (C) 2017 Matt Molyneaux
#
# This file is part of The Houses.
#
# The Houses is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# The Houses is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with The Houses.  If not, see <http://www.gnu.org/licenses/>.
##

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

    def step(self):
        for house in self.houses:
            yield house.step()

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
