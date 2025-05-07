from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from ..db import db
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.planet import Planet 

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] # additional attribute
    description: Mapped[str]
    size: Mapped[str]
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="moons")

    def to_dict(self):
        moon_as_dict = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "size": self.size
        }

        if self.planet:
            moon_as_dict["planet"] = self.planet.name

        return moon_as_dict
    
    @classmethod
    def from_dict(cls, moon_data):
        planet_id = moon_data.get("planet_id")

        new_moon = cls(
            name=moon_data["name"],
            description=moon_data["description"],
            size=moon_data["size"],
            planet_id=planet_id
            )
        return new_moon