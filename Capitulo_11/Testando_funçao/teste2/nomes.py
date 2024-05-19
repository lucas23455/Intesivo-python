import unittest
from teste2 import usuario

class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = usuario('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = usuario('lucas', 'souza', 'passos')
        self.assertEqual(formatted_name, 'Lucas Souza Passos')

if __name__ == '__main__':
    unittest.main()
