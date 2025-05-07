from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.moon import Moon 

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    color: Mapped[str]
    moons: Mapped[list["Moon"]] = relationship(back_populates="planet")

    # instance method, returns existent record as dict 
    def to_dict(self):
        planet_as_dict = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "color": self.color
        }

        if self.moons:
            planet_as_dict["moons"] = [moon.to_dict() for moon in self.moons]

        return planet_as_dict
        
    # class method, creates a new instance of Planet from dict (planet_data)
    @classmethod
    def from_dict(cls, planet_data):
        new_planet = cls(name=planet_data["name"],
                            description=planet_data["description"],
                            color=planet_data["color"])
        return new_planet
    
    

