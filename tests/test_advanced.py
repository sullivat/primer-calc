# -*- coding: utf-8 -*-

from .context import primer-calc

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_main(self):
        primer-calc.main()


if __name__ == '__main__':
    unittest.main()
