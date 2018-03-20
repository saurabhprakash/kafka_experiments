For running this application:
 - Start zookeeper instance: "> bin/zookeeper-server-start.sh config/zookeeper.properties"
 - Start kafka server: "> bin/kafka-server-start.sh config/server.properties"
 - Create a topic named "test" with a single partition and only one replica: "> bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test"
 
 - Set up the virtualenv and run "pip -r requirements.txt"
 - run "python producer.py" on one console[which produces timestamp on interval of 2 secs]
 - run "python consumer.py" - runs a flask application which can be used to consume the produced messages. Consumed messages can be seen on "localhost:5000"
 
 
Kafka Python client used: https://github.com/dpkp/kafka-python
