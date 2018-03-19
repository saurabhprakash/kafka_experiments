# producer.py

import time
from kafka import KafkaProducer, KafkaClient
from PIL import Image

producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Assign a topic
topic = 'test'

def emitter():
    print(' emitting.....')
    while True:
        producer.send(topic, str(time.time()))
        time.sleep(2)
    print('done emitting')

if __name__ == '__main__':
    emitter()

