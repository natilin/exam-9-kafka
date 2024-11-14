import json
import os

from kafka import KafkaProducer


def producer_send_message(msg):
    producer = KafkaProducer(
        bootstrap_servers=os.environ["BOOTSTRAP_SERVERS"],
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    producer.send(
        os.environ["MESSAGES_ALL_TOPIC"],
        value=msg,
        key=msg["email"].encode("utf-8")
    )