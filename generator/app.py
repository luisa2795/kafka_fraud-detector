from kafka import KafkaProducer
import os
import json
from time import sleep
from transactions import create_random_transaction

#get the URL of the kafka broker via environment variable
KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")
TRANSACTIONS_PER_SECOND = float(os.environ.get("TRANSACTIONS_PER_SECOND"))
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND

if __name__== "__main__":
    #instantiate the producer and set broker that will response to a Metadata API request
    producer=KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        #encode all values as JSON
        value_serializer=lambda value: json.dumps(value).encode()
    )

    while True:
        transaction: dict = create_random_transaction()
        producer.send(TRANSACTIONS_TOPIC, value=transaction)
        print(transaction)  # DEBUG
        sleep(SLEEP_TIME)