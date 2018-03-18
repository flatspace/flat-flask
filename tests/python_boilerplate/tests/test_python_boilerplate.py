#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from python_boilerplate import PythonBoilerplate


class TestPython_boilerplate(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        print('Hello, World!')


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
