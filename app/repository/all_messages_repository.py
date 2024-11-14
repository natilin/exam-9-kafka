from app.db.mongo_database import all_messages_collection


def add_new_message(email):
    added_msg =  all_messages_collection.insert_one(email)
    print(f"new_mail added: {added_msg}")
    return added_msg