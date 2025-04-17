class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

planets = [
    Planet(1, "Earth", "Home planet", "blue"),
    Planet(2, "Venus", "Second planet", "red"),
    Planet(3, "Saturn", "Has rings", "purple")
]
    