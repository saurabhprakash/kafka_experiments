# kafka_experiments

Kafka Python sample tutorial link: https://scotch.io/tutorials/build-a-distributed-streaming-system-with-apache-kafka-and-python

Setup steps:
 - Download link(download the binary instead of source): https://kafka.apache.org/downloads
 - Start zookeeper instance: "> bin/zookeeper-server-start.sh config/zookeeper.properties"
 - Start kafka server: "> bin/kafka-server-start.sh config/server.properties"
 - Create a topic named "test" with a single partition and only one replica: "> bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test"
 - See topic: "> bin/kafka-topics.sh --list --zookeeper localhost:2181"
 - Run the producer and then type a few messages into the console to send to the server:
    ```
      > bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
        This is a message
        This is another message
    ```
 - Kafka also has a command line consumer that will dump out messages to standard output.
    ```
      > bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
      This is a message
      This is another message
    ```
    If you have each of the above commands running in a different terminal then you should now be able to type messages into the producer terminal and see them appear in the consumer terminal.
