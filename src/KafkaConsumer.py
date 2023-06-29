from kafka import KafkaConsumer
from google.cloud import storage
import json


if __name__ == "__main__":
    consumer = KafkaConsumer("stock_market_demo",
                             bootstrap_servers=["35.205.226.35:9092"],
                             value_deserializer=lambda x:
                             json.loads(x.decode("utf-8")))
    consumer = KafkaConsumer(
        "stock_market_demo",
        bootstrap_servers=["35.205.226.35:9092"],  # add your IP here
        value_deserializer=lambda x: json.loads(x.decode('utf-8')))


    storage_client = storage.Client()
    bucket = storage_client.bucket("jsenacas")

    for count, i in enumerate(consumer):
        with bucket.blob("stock_market_{}.json".format(count)).open("w") as file:
            json.dump(i.value, file)