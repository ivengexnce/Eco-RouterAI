import unittest
from app.routes.optimizer import RouteOptimizer
from app.models.route_model import RouteModel

class TestRouteOptimizer(unittest.TestCase):

    def setUp(self):
        self.optimizer = RouteOptimizer()

    def test_optimize_route(self):
        start = (34.0522, -118.2437)  # Example coordinates for Los Angeles
        end = (34.0522, -118.2437)    # Example coordinates for Los Angeles
        expected_route = RouteModel(distance=0, time=0, environmental_impact=0)
        
        optimized_route = self.optimizer.optimize_route(start, end)
        
        self.assertEqual(optimized_route.distance, expected_route.distance)
        self.assertEqual(optimized_route.time, expected_route.time)
        self.assertEqual(optimized_route.environmental_impact, expected_route.environmental_impact)

    def test_route_with_traffic(self):
        start = (34.0522, -118.2437)
        end = (34.0522, -118.2437)
        traffic_conditions = {'heavy': True}
        
        optimized_route = self.optimizer.optimize_route(start, end, traffic_conditions)
        
        self.assertIsNotNone(optimized_route)
        self.assertGreater(optimized_route.time, 0)

    def test_route_with_environmental_factors(self):
        start = (34.0522, -118.2437)
        end = (34.0522, -118.2437)
        environmental_factors = {'low_emission_zones': True}
        
        optimized_route = self.optimizer.optimize_route(start, end, environmental_factors)
        
        self.assertIsNotNone(optimized_route)
        self.assertLess(optimized_route.environmental_impact, 10)  # Example threshold

if __name__ == '__main__':
    unittest.main()