## Kafka

- Partitions preserve ordering of messages.

- Only one consumer from one group can read a partition at a time (else async read can cause messages to arrive out of order.)

- Thus, # of consumer groups can be more than # partitions <font color="orange">but</font> some will have to be inactive. <br>
Example: 8 consumers and 6 partitions means atleast 2 inactive consumers at all times.  


