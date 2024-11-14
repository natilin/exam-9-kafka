from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base


class DeviceInfo(Base):
    __tablename__ = "device_info"
    id = Column(Integer, primary_key=True, autoincrement=True)
    browser = Column(String)
    os = Column(String)
    device_id = Column(String)
    person_id = Column(Integer, ForeignKey("person.id"))

    person = relationship("Person", back_populates="device_info")