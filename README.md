# kafka_experiments

Kafka Python sample tutorial link: https://github.com/saurabhprakash/kafka_experiments/tree/master/sample_python_kafka_module
Official sample link: http://kafka-python.readthedocs.io/en/master/usage.html

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
    
  - Setting up a multi-broker cluster
    ```
     So far we have been running against a single broker, but that's no fun. For Kafka, a single broker is just a cluster of size one, so nothing much changes other than starting a few more broker instances. But just to get feel for it, let's expand our cluster to three nodes (still all on our local machine).

     First we make a config file for each of the brokers (on Windows use the copy command instead):
        > cp config/server.properties config/server-1.properties
        > cp config/server.properties config/server-2.properties
    
     Now edit these new files and set the following properties:
     config/server-1.properties:
         broker.id=1
         listeners=PLAINTEXT://:9093
         log.dir=/tmp/kafka-logs-1

     config/server-2.properties:
         broker.id=2
         listeners=PLAINTEXT://:9094
         log.dir=/tmp/kafka-logs-2
       The broker.id property is the unique and permanent name of each node in the cluster. We have to override the port and log directory only because we are running these all on the same machine and we want to keep the brokers from all trying to register on the same port or overwrite each other's data.

       We already have Zookeeper and our single node started, so we just need to start the two new nodes:
       > bin/kafka-server-start.sh config/server-1.properties &
       ...
       > bin/kafka-server-start.sh config/server-2.properties &
       ...
       
       Now create a new topic with a replication factor of three:
       > bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 3 --partitions 1 --topic my-replicated-topic
       Okay but now that we have a cluster how can we know which broker is doing what? To see that run the "describe topics" command:

       > bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic my-replicated-topic
        Topic:my-replicated-topic   PartitionCount:1    ReplicationFactor:3 Configs:
            Topic: my-replicated-topic  Partition: 0    Leader: 1   Replicas: 1,2,0 Isr: 1,2,0
       Here is an explanation of output. The first line gives a summary of all the partitions, each additional line gives information about one partition. Since we have only one partition for this topic there is only one line.

       "leader" is the node responsible for all reads and writes for the given partition. Each node will be the leader for a randomly selected portion of the partitions.
       "replicas" is the list of nodes that replicate the log for this partition regardless of whether they are the leader or even if they are currently alive.
       "isr" is the set of "in-sync" replicas. This is the subset of the replicas list that is currently alive and caught-up to the leader.
       
       Now let's consume these messages:
        > bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic my-replicated-topic
        my test message 1
        my test message 2

        Now let's test out fault-tolerance. Broker 1 was acting as the leader so let's kill it:
        > ps aux | grep server-1.properties
        7564 ttys002    0:15.91 /System/Library/Frameworks/JavaVM.framework/Versions/1.8/Home/bin/java...
        > kill -9 7564

        Leadership has switched to one of the slaves and node 1 is no longer in the in-sync replica set:
        > bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic my-replicated-topic
        Topic:my-replicated-topic   PartitionCount:1    ReplicationFactor:3 Configs:
            Topic: my-replicated-topic  Partition: 0    Leader: 2   Replicas: 1,2,0 Isr: 2,0
        But the messages are still available for consumption even though the leader that took the writes originally is down:

        > bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic my-replicated-topic
        ...
        my test message 1
        my test message 2
    ```
    
 - Use Kafka Connect to import/export data: Kafka Connect is a tool included with Kafka that imports and exports data to Kafka. It is an extensible tool that runs connectors, which implement the custom logic for interacting with an external system.
  
