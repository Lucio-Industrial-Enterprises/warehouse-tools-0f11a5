import unittest

from warehouse.quantity import parse_quantity


class QuantityTests(unittest.TestCase):
    def test_valid_quantity(self):
        self.assertEqual(parse_quantity("5"), 5)

    def test_whitespace_trimmed(self):
        self.assertEqual(parse_quantity("  10  "), 10)

    def test_zero_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("0")

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("-3")
