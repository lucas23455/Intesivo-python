import unittest
from city_functions import cidade_pais

class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_name = cidade_pais('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_name = cidade_pais('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile – população 5000000')

    def test_city_country_with_uppercase_population(self):
        formatted_name = cidade_pais('LISBON', 'PORTUGAL', 1000000)
        self.assertEqual(formatted_name, 'Lisbon, Portugal – população 1000000')

    def test_city_country_with_mixed_case_population(self):
        formatted_name = cidade_pais('nEw YoRk', 'uSa', 8000000)
        self.assertEqual(formatted_name, 'New York, Usa – população 8000000')

if __name__ == '__main__':
    unittest.main()
