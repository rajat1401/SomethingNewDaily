## Kafka

- Partitions preserve ordering of messages.

- Only one consumer from one group can read a partition at a time (else async read can cause messages to arrive out of order.) but multiple consumers of the same group can parallely read many partition of the topic. <br>
<br>

<img src="/Users/rajat_mac/Documents/SomethingNewDaily/images/kafka.png">
<br>
<br>

- Offsets are maintained per group per partition. 

- Thus, # of consumers of a group can be more than # partitions <font color="orange">but</font> some will have to be inactive. <br>
Example: 8 consumers and 6 partitions means atleast 2 inactive consumers at all times.  


