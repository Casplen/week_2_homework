import unittest

from src.guest import Guest

class TestGuest (unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("John", 10.00, "Wannabe")

    def test_guest_has_name(self):
        self.assertEqual("John", self.guest1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(10.00, self.guest1.wallet)

    def test_guest_remove_cash(self):
        self.guest1.remove_cash(5.00)
        self.assertEqual(5.00, self.guest1.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Wannabe", self.guest1.favourite_song)

    def test_guest_can_cheer(self):
        self.assertEqual("Woo!", self.guest1.cheer())