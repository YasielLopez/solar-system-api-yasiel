class Planet:
    def __init__(self, id, name, description, diameter):
        self.id = id
        self.name = name
        self.description = description
        self.diameter = diameter  # additional attribute

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "diameter": self.diameter
        }
    
    planet_list = [
    Planet(1, "Mercury", "Closest planet to the sun.", 3031.9),
    Planet(2, "Venus", "Second planest closet to the sun", 7520.8),
    Planet(3, "Earth", "Third planet closest to the sun.", 7926.2),
    Planet(4, "Mars", "Fourth planet closest from the sun.", 4212.3)
]