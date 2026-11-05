import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"Disc {i}")))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("One too many")))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)
