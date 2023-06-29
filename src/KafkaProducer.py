import random

import pandas as pd
from kafka import KafkaProducer
from time import sleep
import json


if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers=["35.205.226.35:9092"],
                             value_serializer=lambda x:
                             json.dumps(x).encode("utf-8"))

    df = pd.read_csv("gs://jsenacas/indexProcessed")

    print(df.head())

    for i in range(10):
        dict_stock = df.sample(1).to_dict(orient="records")[0]
        producer.send("stock_market_demo", dict_stock)
        sleep(random.randint(1,2))

    producer.flush()