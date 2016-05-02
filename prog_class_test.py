from bs4 import BeautifulSoup
from prog_class import setup_url
import unittest


class TestStringMethods(unittest.TestCase):

    def test_setup_url(self):
        temp = setup_url('http://rosettacode.org/wiki/Factorial')
        self.assertEqual(type(temp), BeautifulSoup)

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
