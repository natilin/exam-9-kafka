import json
import os


from dotenv import load_dotenv
from kafka import KafkaConsumer

from app.services.email_service import handel_new_message

load_dotenv(verbose=True)




def consumer_hostage_context():
    consumer = KafkaConsumer(
        os.environ["HOSTAGE_MESSAGES_TOPIC"],
        bootstrap_servers=os.environ["BOOTSTRAP_SERVERS"],
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        auto_offset_reset="earliest"
    )
    for message in consumer:
        print(f"Received: {message.key}: {message.value}")
        new_email = message.value
        if handel_new_message(new_email, "hostage"):
            print("new 'hostage' message added")


if __name__ == "__main__":
    consumer_hostage_context()
