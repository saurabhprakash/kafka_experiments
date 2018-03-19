from flask import Flask, Response
from kafka import KafkaConsumer

#connect to Kafka server and pass the topic we want to consume
consumer = KafkaConsumer('test', group_id='view', 
    bootstrap_servers=['0.0.0.0:9092'], auto_offset_reset='earliest')

#Continuously listen to the connection and print messages as recieved
app = Flask(__name__)

@app.route('/')
def index():
    return Response(kafkastream())

def kafkastream():
    for msg in consumer:
        print (msg.value)
        yield (msg.value + '\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
