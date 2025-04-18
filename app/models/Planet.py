class Planet:
    def __init__(self, id, name, description, diameter_km):
        self.id = id
        self.name = name
        self.description = description
        self.diameter_km = diameter_km  # Additional attribute
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "diameter_km": self.diameter_km
        }
