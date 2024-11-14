from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base


class DeviceInfo(Base):
    _tablename_ = "person"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    created_at = Column(String, nullable=False)

    location = relationship("Location", back_populates="person", uselist=False)
    device_info = relationship("DeviceInfo", back_populates="person", uselist=False)
    explosive_contents = relationship("ExplosiveContent", back_populates="person")
    hostage_contents = relationship("HostageContent", back_populates="person")