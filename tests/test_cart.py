import unittest
from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i + 1}", "Test", 10.0)))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21", "Test", 10.0)))

    def test_total_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD 1", "Test", 19.95))
        cart.add_dvd(DigitalVideoDisc("DVD 2", "Test", 24.95))
        self.assertEqual(cart.total_cost(), 44.90)

    def test_total_cost_with_discount(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD 1", "Test", 100.0))
        self.assertEqual(cart.total_cost_with_discount(20), 80.0)

    def test_total_cost_with_invalid_discount(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD 1", "Test", 100.0))
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)


if __name__ == "__main__":
    unittest.main()
