# producer.py
import time
import json

from kafka import KafkaProducer

# producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer = KafkaProducer(bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Assign a topic
topic = 'test'


def emitter():
    print(' emitting.....')
    while True:
        _time = str(time.time())
        producer.send(topic, {'foo': _time})
        # producer.send(topic, str(time.time()))
        time.sleep(2)
    print('done emitting')


if __name__ == '__main__':
    emitter()
