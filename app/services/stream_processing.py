import os
from dotenv import load_dotenv
import faust

from app.utils.message_process_utils import find_suspicious_words

load_dotenv(verbose=True)


suspicious_words = ["explos", "hostage"]

app = faust.App(
    "email_processing",  # App name
    broker=os.environ['BOOTSTRAP_SERVERS'],  # Kafka broker
    value_serializer='json'  # Message value format
)


all_message_topic = app.topic(os.environ["ALL_MESSAGES_TOPIC"])


processed_exploding_msg_topic = app.topic(os.environ["EXPLOSIVE_MESSAGES_TOPIC"])
processed_hostage_msg_topic = app.topic(os.environ["HOSTAGE_MESSAGES_TOPIC"])




# Define a data model for the processed message
class ProcessedMessage(faust.Record, serializer='json'):
    email: str
    username: str
    ip_address: str
    created_at: str
    location: dict
    device_info: dict
    sentences: list




# Stream processing agent
@app.agent(all_message_topic)
async def process_message(messages):
    async for message in messages:

        suspicious_word = find_suspicious_words(message["sentences"], suspicious_words)

        processed_message = ProcessedMessage(
            email=message["email"],
            username=message['username'],
            ip_address = message["ip_address"],
            created_at=message["created_at"],
            location=message["location"],
            device_info=message["device_info"],
            sentences=message["sentences"]
        )


        if "explos" in suspicious_word:

            # Produce the processed message to the output topic
            await processed_exploding_msg_topic.send(value=processed_message)
            print(f"Processed and sent processed_exploding_msg_topic")
        elif "hostage" in suspicious_word:
            await processed_hostage_msg_topic.send(value=processed_message)
            print(f"Processed and sent to processed_hostage_msg_topic")


if __name__ == '__main__':
    # Run Faust in one thread
    app.main()