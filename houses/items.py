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

from __future__ import division


class PhysicalObject(object):
    can_be_carried = False
    name = "PhysicalObject"
    health_total = 100
    _health_now = 100

    @property
    def health(self):
        return self._health_now / self.health_total

    @health.setter
    def health(self, value):
        self._health_now = min(max(value, 0), self.health_total)

    def can_have_on(self, obj):
        """Can this object have obj on it?

        Be careful not to call can_be_on to avoid infinite recursion

        E.g. Wall().can_have_on(Door()) is True, but Door().can_have_on(Wall())
        is False
        """
        return False

    def can_be_on(self, obj):
        """Can this object be placed onto obj?

        Be careful not to call can_have_on to avoid infinite recursion

        E.g. Door().can_be_on(Wall()) is True, but Door().can_be_on(None) is
        False
        """
        return obj is None


class Wall(PhysicalObject):
    name = "Wall"

    def can_have_on(self, obj):
        return True


class Door(PhysicalObject):
    name = "Door"
    is_open = False
    is_locked = False

    def can_be_on(self, obj):
        return isinstance(obj, Wall)


class Table(PhysicalObject):
    name = "Table"

    def can_have_no(self, obj):
        return True


class Chair(PhysicalObject):
    name = "Chair"


class Bed(PhysicalObject):
    name = "Bed"
