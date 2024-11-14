from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.models import Base


class Person(Base):
   __tablename__ = "person"
   id = Column(Integer, primary_key=True, autoincrement=True)
   region = Column(String)
   capital = Column(String)
   name = Column(String)
   vacations = relationship("Student_vacation", back_populates="country")
