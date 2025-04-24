from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    color: Mapped[str]











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
    