import unittest
from teste1 import usuario

class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = usuario('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()
