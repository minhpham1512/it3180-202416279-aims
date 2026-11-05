import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.items = [
            DigitalVideoDisc("The Lion King", "Animation"),
            DigitalVideoDisc("Star Wars", "Science Fiction"),
            DigitalVideoDisc("Aladdin", "Animation"),
        ]

    def test_search_by_title(self):
        result = search_by_title(self.items, "Star")
        self.assertEqual([d.title for d in result], ["Star Wars"])
