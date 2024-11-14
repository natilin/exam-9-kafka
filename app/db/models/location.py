from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.db.models import Base


class Location(Base):
    _tablename_ = "location"
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float)
    longitude = Column(Float)
    city = Column(String)
    country = Column(String)
    person_id = Column(Integer, ForeignKey("person.id"))

    person = relationship("Person", back_populates="location")