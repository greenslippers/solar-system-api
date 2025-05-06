from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    color: Mapped[str]

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(name=planet_data["name"],
                            description=planet_data["description"],
                            color=planet_data["color"])
        return new_planet
    
    def to_dict(self):
        planet_as_dict = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "color": self.color
        }

        return planet_as_dict









# class Planet:
#     def __init__(self, id, name, description, color):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.color = color

# planets = [
#     Planet(1, "Earth", "Home planet", "blue"),
#     Planet(2, "Venus", "Second planet", "red"),
#     Planet(3, "Saturn", "Has rings", "purple")
# ]
    