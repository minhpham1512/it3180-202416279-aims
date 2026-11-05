import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.items = [
            DigitalVideoDisc("The Lion King", "Animation"),
            DigitalVideoDisc("Star Wars", "Science Fiction"),
            DigitalVideoDisc("Aladdin", "Animation"),
        ]

    def test_search_by_category(self):
        result = search_by_category(self.items, "animation")
        self.assertEqual([d.title for d in result], ["The Lion King", "Aladdin"])

    def test_search_by_title(self):
        result = search_by_title(self.items, "Star")
        self.assertEqual([d.title for d in result], ["Star Wars"])

    def test_search_by_title_is_case_insensitive(self):
        result = search_by_title(self.items, "lion")
        self.assertEqual([d.title for d in result], ["The Lion King"])
