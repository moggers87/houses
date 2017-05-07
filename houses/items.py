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
