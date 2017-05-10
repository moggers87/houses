##
# Copyright (C) 2017 Matt Molyneaux
#
# This file is part of CimCity.
#
# CimCity is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CimCity is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CimCity.  If not, see <http://www.gnu.org/licenses/>.
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

    def test_add(self):
        pass

    def test_remove(self):
        pass

    def test_magic_contains(self):
        pass
