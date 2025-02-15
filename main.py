"""
This class runs the pipeline
"""

from kafka_producer import KafkaDataProducer
from kafka_consumer import KafkaDataConsumer

if __name__ == "__main__":
    producer = KafkaDataProducer()
    producer.stream_data()

    consumer = KafkaDataConsumer()
    consumer.consume()