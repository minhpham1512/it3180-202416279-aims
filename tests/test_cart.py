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


class TestCartDiscount(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("Disc A", cost=60.0))
        self.cart.add_dvd(DigitalVideoDisc("Disc B", cost=40.0))

    def test_discount_returns_discounted_total(self):
        self.assertAlmostEqual(self.cart.total_cost_with_discount(20), 80.0)

    def test_discount_rejects_invalid_percent(self):
        with self.assertRaises(ValueError):
            self.cart.total_cost_with_discount(150)
