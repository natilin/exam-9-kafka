from sqlalchemy.orm import declarative_base
Base = declarative_base()

from .person import Person
from .location import Location
from .device_info import DeviceInfo
from .hostage_content import HostageContent
from .explosive_content import ExplosiveContent