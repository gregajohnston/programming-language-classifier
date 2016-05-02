from bs4 import BeautifulSoup
from prog_class import setup_url, find_example_urls
import unittest


class TestStringMethods(unittest.TestCase):

    def test_setup_url(self):
        temp_soup = setup_url('http://rosettacode.org/wiki/Factorial')
        self.assertEqual(type(temp_soup), BeautifulSoup)

    def test_find_example_urls(self):
        temp_soup = setup_url('http://rosettacode.org/wiki/Factorial')
        temp_url = find_example_urls(temp_soup)
        print(temp_url)
        self.assertEqual(type(temp_url), list)

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
