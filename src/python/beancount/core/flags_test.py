__author__ = "Martin Blais <blais@furius.ca>"

import unittest

from beancount.core import flags


class TestFlags(unittest.TestCase):

    ALLOW_NOT_UNIQUE = {'FLAG_IMPORT'}

    def test_unique_flags(self):
        names = set()
        values = set()
        for name, value in flags.__dict__.items():
            # pylint: disable=bad-continuation
            if (not name.startswith("FLAG_") or
                name in self.ALLOW_NOT_UNIQUE):
                continue
            names.add(name)
            values.add(value)
        self.assertEqual(len(names), len(values))
