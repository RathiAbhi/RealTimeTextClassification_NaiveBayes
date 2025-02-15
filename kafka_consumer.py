"""
Consumes kafka messages, summarizes text, and sends to classifier
"""

from kafka import KafkaConsumer
import json
from text_summarizer import TextSummarizer
from text_classifier import TextClassifier
from config import KAFKA_TOPIC,KAFKA_SERVER,OPENAI_API_KEY

class KafkaDataConsumer:
    def __init__(self):
        self.consumer = KafkaConsumer(
            KAFKA_TOPIC,
            bootstrap_servers = KAFKA_SERVER,
            auto_offset_reset='earliest',
            value_deserializer = lambda x:json.loads(x.decode('utf-8'))
        )

    def consume(self):
        summarizer = TextSummarizer(OPENAI_API_KEY)
        classifier = TextClassifier()

        for message in self.consumer:
            data = message.value
            summarized_text = summarizer.summarize(data.get("bio",""))
            text_type = classifier.predict(summarized_text)
            print(f"User: {data['name']} | Type: {text_type}")