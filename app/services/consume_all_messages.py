import json
import os


from dotenv import load_dotenv
from kafka import KafkaConsumer, KafkaProducer

from app.utils.message_process_utils import find_suspicious_words

load_dotenv(verbose=True)

suspicious_words = ["explos", "hostage"]


def consumer_split_msg_by_context():
    consumer = KafkaConsumer(
        os.environ["ALL_MESSAGES_TOPIC"],
        bootstrap_servers=os.environ["BOOTSTRAP_SERVERS"],
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        auto_offset_reset="latest"
    )
    for message in consumer:
        print(f"Received: {message.key}: {message.value}")
        new_email = message.value
        suspicious_word = find_suspicious_words(new_email["sentences"], suspicious_words)

        if "explos" in suspicious_word:

            producer_explosive_message(new_email)
            print("sent processed_exploding_msg_topic")
        elif "hostage" in suspicious_word:
            producer_hostage_message(new_email)
            print("sent to processed_hostage_msg_topic")

def producer_hostage_message(msg):
    producer = KafkaProducer(
        bootstrap_servers=os.environ["BOOTSTRAP_SERVERS"],
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    producer.send(
        os.environ["HOSTAGE_MESSAGES_TOPIC"],
        value=msg,
        key=msg["email"].encode("utf-8")
    )

def producer_explosive_message(msg):
    producer = KafkaProducer(
        bootstrap_servers=os.environ["BOOTSTRAP_SERVERS"],
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    producer.send(
        os.environ["EXPLOSIVE_MESSAGES_TOPIC"],
        value=msg,
        key=msg["email"].encode("utf-8")
    )

if __name__ == "__main__":
    consumer_split_msg_by_context()