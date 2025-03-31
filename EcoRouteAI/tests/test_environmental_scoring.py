import unittest
from app.services.environmental_scoring import EnvironmentalScoringService

class TestEnvironmentalScoringService(unittest.TestCase):

    def setUp(self):
        self.scoring_service = EnvironmentalScoringService()

    def test_calculate_score_low_emissions(self):
        route_data = {
            'distance': 10,  # in kilometers
            'fuel_consumption': 5,  # in liters
            'co2_emissions': 12  # in kg
        }
        score = self.scoring_service.calculate_score(route_data)
        self.assertLess(score, 50)  # Assuming lower scores are better

    def test_calculate_score_high_emissions(self):
        route_data = {
            'distance': 10,  # in kilometers
            'fuel_consumption': 15,  # in liters
            'co2_emissions': 30  # in kg
        }
        score = self.scoring_service.calculate_score(route_data)
        self.assertGreater(score, 50)  # Assuming higher scores are worse

    def test_calculate_score_edge_case(self):
        route_data = {
            'distance': 0,  # in kilometers
            'fuel_consumption': 0,  # in liters
            'co2_emissions': 0  # in kg
        }
        score = self.scoring_service.calculate_score(route_data)
        self.assertEqual(score, 0)  # No emissions should yield a score of 0

if __name__ == '__main__':
    unittest.main()