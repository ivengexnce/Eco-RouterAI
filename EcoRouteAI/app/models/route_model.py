class RouteModel:
    def __init__(self, start_point, end_point, distance, time, environmental_impact):
        self.start_point = start_point
        self.end_point = end_point
        self.distance = distance  # in kilometers
        self.time = time          # in minutes
        self.environmental_impact = environmental_impact  # CO2 emissions in grams

    def __repr__(self):
        return (f"RouteModel(start_point={self.start_point}, end_point={self.end_point}, "
                f"distance={self.distance}, time={self.time}, environmental_impact={self.environmental_impact})")

    def get_route_info(self):
        return {
            "start_point": self.start_point,
            "end_point": self.end_point,
            "distance": self.distance,
            "time": self.time,
            "environmental_impact": self.environmental_impact
        }