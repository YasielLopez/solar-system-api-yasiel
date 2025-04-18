class Planet:
    def __init__(self, id, name, description, diameter_km):
        self.id = id
        self.name = name
        self.description = description
        self.diameter_km = diameter_km
    
    # creates a to_dict() method that converts the object to a dictionary format suitable for JSON responses
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "diameter_km": self.diameter_km
        }
