from app.db.models import Person
from app.db.psql_database import session_maker


def add_new_person(new_person: Person):
    with session_maker() as session:
        session.add(new_person)
        session.commit()
        session.refresh(new_person)
        return new_person