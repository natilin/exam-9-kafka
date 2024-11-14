from app.db.models import Person, Location, DeviceInfo, ExplosiveContent, HostageContent
from app.repository.person_repository import add_new_person


def handel_new_message(new_email: dict, content: str):
    person = Person(
        email=new_email["email"],
        username=new_email["username"],
        ip_address=new_email["ip_address"],
        created_at=new_email["created_at"]
    )
    location = Location(
        latitude=new_email["latitude"],
        longitude=new_email["longitude"],
        city=new_email["city"],
        country=new_email["country"]
    )
    device_info = DeviceInfo(
        browser=new_email["browser"],
        os=new_email["os"],
        device_id=new_email["device_id"]
    )
    person.location = location
    person.device_info = device_info

    if content == "explosive":
        explosive_content = ExplosiveContent(
            sentence=new_email["sentence"]
        )
        person.explosive_contents = explosive_content

    elif content == "hostage":
       hostage_content =  HostageContent(
           sentence=new_email["sentence"]
       )
       person.hostage_contents = hostage_content

    return add_new_person(person)
