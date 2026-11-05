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


class TestCartSort(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("Star Wars", cost=24.95))
        self.cart.add_dvd(DigitalVideoDisc("Aladdin", cost=18.99))
        self.cart.add_dvd(DigitalVideoDisc("Aladdin", cost=20.0))

    def test_sort_by_title(self):
        self.cart.sort_by_title()
        self.assertEqual([(d.title, d.cost) for d in self.cart.items],
                         [("Aladdin", 20.0), ("Aladdin", 18.99), ("Star Wars", 24.95)])

    def test_sort_by_cost(self):
        self.cart.sort_by_cost()
        self.assertEqual([d.cost for d in self.cart.items], [24.95, 20.0, 18.99])
