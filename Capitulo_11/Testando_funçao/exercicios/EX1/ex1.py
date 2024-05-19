import unittest
from city_functions import cidade_pais

class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_name = cidade_pais('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_with_uppercase(self):
        formatted_name = cidade_pais('LISBON', 'PORTUGAL')
        self.assertEqual(formatted_name, 'Lisbon, Portugal')

    def test_city_country_with_mixed_case(self):
        formatted_name = cidade_pais('nEw YoRk', 'uSa')
        self.assertEqual(formatted_name, 'New York, Usa')

if __name__ == '__main__':
    unittest.main()
