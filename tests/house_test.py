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

from unittest import TestCase

from houses.house import House, ThingsInHouse
from houses.items import PhysicalObject


class HouseTestCase(TestCase):
    def test_init(self):
        house = House(name="Bob's house", plot_size=(100, 120))

        self.assertEqual(house.name, "Bob's house")
        self.assertEqual(house.plot_size, (100, 120))

        with self.assertRaises(TypeError):
            House(name="Bob's other house", plot_size=None)


class ThingsInHouseTestCase(TestCase):
    def setUp(self):
        self.house = House(name="Bob's house", plot_size=(100, 120))
        self.things = ThingsInHouse(self.house)

    def test_get(self):
        self.assertEqual(self.things.get((1, 1)), None)

        with self.assertRaises(KeyError):
            self.things[(1, 1)]

        self.things._objects[(1, 1)] = ["thing"]
        self.assertEqual(self.things[(1, 1)], ["thing"])
        self.assertEqual(self.things.get((1, 1)), ["thing"])

        with self.assertRaises(TypeError):
            self.things.get(None)

        with self.assertRaises(TypeError):
            self.things[None]

    def test_add(self):
        obj = PhysicalObject()
        self.things.add((1, 1), obj)

        self.assertEqual(self.things.get((1, 1)), [obj])

        with self.assertRaises(TypeError):
            self.things.add(None, obj)

        # will error because PhysicalObjects can't sit on top of eachother
        with self.assertRaises(KeyError):
            self.things.add((1, 1), obj)

        # out of bounds
        with self.assertRaises(KeyError):
            self.things.add((200, 200), obj)

    def test_remove(self):
        obj = PhysicalObject()
        obj2 = PhysicalObject()

        with self.assertRaises(TypeError):
            self.things.remove(None, obj)

        with self.assertRaises(KeyError):
            self.things.remove((1, 1), obj)

        self.things.add((1, 1), obj)
        with self.assertRaises(ValueError):
            self.things.remove((1, 1), obj2)

        self.things._objects[(1, 1)].append(obj2)
        with self.assertRaises(ValueError):
            self.things.remove((1, 1), obj)

        self.things.remove((1, 1), obj2)
        self.assertEqual(self.things[(1, 1)], [obj])

        self.things.remove((1, 1), obj)
        with self.assertRaises(KeyError):
            self.things[(1, 1)]

        with self.assertRaises(KeyError):
            self.things.remove((100000, 10000000), obj)

    def test_magic_contains(self):
        self.assertFalse((1, 1) in self.things)

        with self.assertRaises(TypeError):
            PhysicalObject() in self.things

        self.things.add((1, 1), PhysicalObject())
        self.assertTrue((1, 1) in self.things)

        with self.assertRaises(TypeError):
            PhysicalObject() in self.things
