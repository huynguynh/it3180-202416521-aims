import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title


class TestSearch(unittest.TestCase):
    def test_search_by_category(self):
        items = [
            DigitalVideoDisc("The Lion King", "Animation", 19.95),
            DigitalVideoDisc("Star Wars", "Science Fiction", 24.95),
            DigitalVideoDisc("Aladdin", "Animation", 18.99),
        ]
        result = search_by_category(items, "animation")
        self.assertEqual([d.title for d in result], ["The Lion King", "Aladdin"])

    def test_search_by_title_case_insensitive(self):
        items = [
            DigitalVideoDisc("The Lion King", "Animation", 19.95),
            DigitalVideoDisc("Star Wars", "Science Fiction", 24.95),
        ]
        result = search_by_title(items, "lion")
        self.assertEqual([d.title for d in result], ["The Lion King"])


if __name__ == "__main__":
    unittest.main()
