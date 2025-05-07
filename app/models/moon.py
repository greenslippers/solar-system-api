from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] # additional attribute
    description: Mapped[str]
    size: Mapped[str]

    def to_dict(self):
        moon_as_dict = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "size": self.size
        }

        return moon_as_dict
    
    @classmethod
    def from_dict(cls, moon_data):
        new_moon = Moon(name=moon_data["name"],
                            description=moon_data["description"],
                            size=moon_data["size"])
        return new_moon