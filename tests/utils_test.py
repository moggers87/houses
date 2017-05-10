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

from houses import utils


class UtilsTestCase(TestCase):
    def test_is_two_int_tuple(self):
        self.assertEqual(utils.is_two_int_tuple((0, 1)), True)
        self.assertEqual(utils.is_two_int_tuple((0,)), False)
        self.assertEqual(utils.is_two_int_tuple([0, 1]), False)
        self.assertEqual(utils.is_two_int_tuple(("", "")), False)
        self.assertEqual(utils.is_two_int_tuple((1.0, 2.0)), False)
