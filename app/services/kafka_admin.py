import os

from dotenv import load_dotenv
from kafka import KafkaAdminClient
from kafka.admin import NewTopic

load_dotenv(verbose=True)

topics = [
   {"name": os.environ["ALL_MESSAGES_TOPIC"], "partitions": 3, "replication": 1},
    {"name": os.environ["EXPLOSIVE_MESSAGES_TOPIC"], "partitions": 3, "replication": 1},
    {"name": os.environ["HOSTAGE_MESSAGES_TOPIC"], "partitions": 3, "replication": 1},
]

def init_topics():
   admin_client = KafkaAdminClient(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])
   topic_list = [
       NewTopic(
               name=topic["name"],
               num_partitions=topic["partitions"],
               replication_factor=topic["replication"]
           ) for topic in topics
   ]


   try:
       admin_client.create_topics(new_topics=topic_list, validate_only=False)
       print("Topics created successfully!")
   except Exception as e:
       print(f"Error creating topics: {e}")
   finally:
       admin_client.close()

if __name__ == "__main__":
    init_topics()
