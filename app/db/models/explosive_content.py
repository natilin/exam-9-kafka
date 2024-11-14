from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base


class ExplosiveContent(Base):
    _tablename_ = "suspicious_explosive_content"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sentence = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey("person.id"))

    person = relationship("Person", back_populates="explosive_contents")