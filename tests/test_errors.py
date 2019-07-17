# -*- coding: utf-8 -*-
# Copyright (C) 2019 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import unittest

from gvm.errors import InvalidArgument, RequiredArgument, GvmError


class InvalidArgumentTestCase(unittest.TestCase):
    def test_raise_with_message(self):
        with self.assertRaisesRegex(InvalidArgument, '^foo bar$'):
            raise InvalidArgument('foo bar')

    def test_message_precedence(self):
        with self.assertRaisesRegex(InvalidArgument, '^foo bar$') as cm:
            raise InvalidArgument('foo bar', argument='foo', function='bar')

        ex = cm.exception
        self.assertEqual(ex.argument, 'foo')
        self.assertEqual(ex.function, 'bar')

        self.assertEqual(str(ex), 'foo bar')

    def test_raise_with_argument(self):
        with self.assertRaises(InvalidArgument) as cm:
            raise InvalidArgument(argument='foo')

        ex = cm.exception
        self.assertEqual(ex.argument, 'foo')
        self.assertIsNone(ex.function)

    def test_raise_with_function(self):
        with self.assertRaises(InvalidArgument) as cm:
            raise InvalidArgument(function='foo')

        ex = cm.exception
        self.assertEqual(ex.function, 'foo')
        self.assertIsNone(ex.argument)

    def test_raise_with_argument_and_function(self):
        with self.assertRaises(InvalidArgument) as cm:
            raise InvalidArgument(argument='foo', function='bar')

        ex = cm.exception
        self.assertEqual(ex.argument, 'foo')
        self.assertEqual(ex.function, 'bar')

    def test_string_conversion(self):
        with self.assertRaises(InvalidArgument) as cm:
            raise InvalidArgument('foo bar', argument='foo')

        ex = cm.exception
        self.assertEqual(str(ex), 'foo bar')

        with self.assertRaises(InvalidArgument) as cm:
            raise InvalidArgument(argument='foo')

        ex = cm.exception
        self.assertEqual(str(ex), 'Invalid argument foo')

        with self.assertRaises(InvalidArgument) as cm:
            raise InvalidArgument(function='foo')

        ex = cm.exception
        self.assertEqual(str(ex), 'Invalid argument for foo')

        with self.assertRaises(InvalidArgument) as cm:
            raise InvalidArgument(argument='foo', function='bar')

        ex = cm.exception
        self.assertEqual(str(ex), 'Invalid argument foo for bar')

    def test_is_gvm_error(self):
        with self.assertRaises(GvmError):
            raise InvalidArgument('foo bar')


class RequiredArgumentTestCase(unittest.TestCase):
    def test_raise_with_message(self):
        with self.assertRaisesRegex(RequiredArgument, '^foo bar$'):
            raise RequiredArgument('foo bar')

    def test_message_precedence(self):
        with self.assertRaisesRegex(RequiredArgument, '^foo bar$') as cm:
            raise RequiredArgument('foo bar', argument='foo', function='bar')

        ex = cm.exception
        self.assertEqual(ex.argument, 'foo')
        self.assertEqual(ex.function, 'bar')

        self.assertEqual(str(ex), 'foo bar')

    def test_raise_with_argument(self):
        with self.assertRaises(RequiredArgument) as cm:
            raise RequiredArgument(argument='foo')

        ex = cm.exception
        self.assertEqual(ex.argument, 'foo')
        self.assertIsNone(ex.function)

    def test_raise_with_function(self):
        with self.assertRaises(RequiredArgument) as cm:
            raise RequiredArgument(function='foo')

        ex = cm.exception
        self.assertEqual(ex.function, 'foo')
        self.assertIsNone(ex.argument)

    def test_raise_with_argument_and_function(self):
        with self.assertRaises(RequiredArgument) as cm:
            raise RequiredArgument(argument='foo', function='bar')

        ex = cm.exception
        self.assertEqual(ex.argument, 'foo')
        self.assertEqual(ex.function, 'bar')

    def test_string_conversion(self):
        with self.assertRaises(RequiredArgument) as cm:
            raise RequiredArgument('foo bar')

        ex = cm.exception
        self.assertEqual(str(ex), 'foo bar')

        with self.assertRaises(RequiredArgument) as cm:
            raise RequiredArgument(argument='foo')

        ex = cm.exception
        self.assertEqual(str(ex), 'Required argument foo')

        with self.assertRaises(RequiredArgument) as cm:
            raise RequiredArgument(function='foo')

        ex = cm.exception
        self.assertEqual(str(ex), 'Required argument missing for foo')

        with self.assertRaises(RequiredArgument) as cm:
            raise RequiredArgument(argument='foo', function='bar')

        ex = cm.exception
        self.assertEqual(str(ex), 'bar requires a foo argument')

    def test_is_gvm_error(self):
        with self.assertRaises(GvmError):
            raise RequiredArgument('foo bar')


if __name__ == '__main__':
    unittest.main()