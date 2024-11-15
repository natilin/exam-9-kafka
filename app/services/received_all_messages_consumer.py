import json
import os


from dotenv import load_dotenv

from kafka import KafkaConsumer

from app.db.mongo_database import init_mongo_db
from app.repository.all_messages_repository import add_new_message

load_dotenv(verbose=True)




def consumer_get_all_message():
    consumer = KafkaConsumer(
        os.environ["ALL_MESSAGES_TOPIC"],
        bootstrap_servers=os.environ["BOOTSTRAP_SERVERS"],
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        auto_offset_reset="latest"
    )
    for message in consumer:
        print(f"Received: {message.key}: {message.value}")
        new_email = message.value
        add_new_message(new_email)


if __name__ == "__main__":
    init_mongo_db()
    consumer_get_all_message()