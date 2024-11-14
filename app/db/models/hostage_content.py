from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base


class HostageContent(Base):
    _tablename_ = "suspicious_hostage_content"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sentence = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey("person.id"))

    person = relationship("Person", back_populates="hostage_contents")