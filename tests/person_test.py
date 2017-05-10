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

from houses import person


class PersonTestCase(TestCase):
    def test_init(self):
        p = person.Person(name="Bob")

        self.assertEqual(p.name, "Bob")
        self.assertEqual(p.can_be_on(p), False)
        self.assertEqual(p.can_have_on(p), False)
        self.assertEqual(p.can_be_on(None), True)
