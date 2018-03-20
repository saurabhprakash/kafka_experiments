import json

from flask import Flask, Response
from kafka import KafkaConsumer

# Current consumer always picks those tasks post past processed offset.
consumer = KafkaConsumer(group_id='test', bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('ascii')))

consumer.subscribe(['test'])

# Continuously listen to the connection and print messages as recieved
app = Flask(__name__)


@app.route('/')
def index():
    return Response(kafkastream())


def kafkastream():
    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
            message.offset, message.key, message.value))
        # consumer.commit()
        yield (str(message.value) + '\n')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
