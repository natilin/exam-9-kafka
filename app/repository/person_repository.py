from app.db.models import Person, ExplosiveContent, HostageContent
from app.db.psql_database import session_maker
from returns.maybe import Maybe


def add_new_person(new_person: Person):
    with session_maker() as session:
        session.add(new_person)
        session.commit()
        session.refresh(new_person)
        return new_person




def get_context_by_email(email) -> dict:
        with session_maker() as session:
            context =  (
                session.query(Person)
                .filter(email == Person.email)
                .first()
            )
            hostage_list =[]
            exploding_list = []
            if context is not None:
                if context.hostage_contents:
                    for sentece in context.hostage_contents:
                        hostage_list.append(sentece.sentence)

                if context.explosive_contents:
                    for sentece in context.explosive_contents:
                        exploding_list.append(sentece.sentence)
                return {
                    "id":context.id,
                    "email":context.email,
                    "username":context.username,
                    "ip_address":context.ip_address,
                    "explosive_contents": exploding_list,
                    "hostage_contents": hostage_list,
                    "created_at":context.created_at

                }
            return {}





