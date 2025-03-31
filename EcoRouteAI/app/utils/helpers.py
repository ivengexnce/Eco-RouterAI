def format_route_data(route_data):
    """Format route data for display or logging."""
    return {
        "distance": f"{route_data['distance']} km",
        "time": f"{route_data['time']} mins",
        "environmental_impact": f"{route_data['environmental_impact']} CO2 kg"
    }

def parse_api_response(response):
    """Parse the API response and extract relevant data."""
    try:
        data = response.json()
        return data.get('routes', [])
    except ValueError:
        return []

def calculate_priority_score(route, user_priorities):
    """Calculate a score for the route based on user-defined priorities."""
    score = 0
    if user_priorities.get('shortest'):
        score -= route['distance']
    if user_priorities.get('fastest'):
        score -= route['time']
    if user_priorities.get('eco_friendly'):
        score += route['environmental_impact']
    return score

def log_route_selection(route):
    """Log the selected route for analytics."""
    print(f"Selected Route: {route['id']} - Distance: {route['distance']} km, Time: {route['time']} mins")