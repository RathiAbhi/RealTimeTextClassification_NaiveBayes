"""
This class streams scraped data to kafka
"""

from kafka import KafkaProducer
import json
from data_fetcher import DataFetcher
from config import KAFKA_TOPIC, KAFKA_SERVER

class KafkaDataProducer:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_SERVER,
            value_serializer=lambda v:json.dumps(v).encode('utf-8')
        )

    def stream_data(self):
        fetcher = DataFetcher()
        data = fetcher.fetch_from_mongo()
        for entry in data:
            self.producer.send(KAFKA_TOPIC,entry)
            print(f"Sent: {entry['name']}")

if __name__ == "__main__":
    KafkaDataProducer.stream_data()