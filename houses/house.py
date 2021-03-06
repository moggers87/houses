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

from houses import utils


class House(object):
    def __init__(self, name, plot_size):
        self.name = name
        if not utils.is_two_int_tuple(plot_size):
            raise TypeError("plot_size must be a tuple of two ints")
        self.plot_size = plot_size

        self.items = ThingsInHouse(self)


class ThingsInHouse(object):
    def __init__(self, house):
        self.house = house
        self._objects = {}

    def check_key_in_bounds(self, key):
        contraints = [
            key[0] >= 0,
            key[1] >= 0,
            key[0] < self.house.plot_size[0],
            key[1] < self.house.plot_size[1],
        ]

        return all(contraints)

    def __getitem__(self, key):
        if not utils.is_two_int_tuple(key):
            raise TypeError("key must be a tuple of two ints")

        return self._objects[key]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def add(self, key, item):
        if not utils.is_two_int_tuple(key):
            raise TypeError("key must be a tuple of two ints")
        if not self.check_key_in_bounds(key):
            raise KeyError("Out of bounds")

        if key in self._objects:
            if item in self._objects[key]:
                raise ValueError("This item is already at this place")

            top_item = self._objects[key][-1]
            if top_item.can_have_on(item) and item.can_be_on(top_item):
                self._objects[key].append(item)
            else:
                raise KeyError("Something already here")
        else:
            self._objects[key] = [item]

    def remove(self, key, item):
        if not utils.is_two_int_tuple(key):
            raise TypeError("key must be a tuple of two ints")
        if not self.check_key_in_bounds(key):
            raise KeyError("Out of bounds")

        items = self._objects[key]
        if items[-1] is item:
            if len(items) <= 1:
                del self._objects[key]
            else:
                items.pop()
        else:
            raise ValueError("%s was not removable" % item)

    def __contains__(self, key):
        if not utils.is_two_int_tuple(key):
            raise TypeError("key must be a tuple of two ints")

        return key in self._objects
