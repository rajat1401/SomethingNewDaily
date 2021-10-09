## Distributed transaction  and 2 Phase Commit Protocol <br>

1. <font color="cyan">Distributed transaction</font> <br>
A transaction with ACID acroos multiple data sources. 

<img src="/Users/rajat_mac/Documents/SomethingNewDaily/images/transaction1.png"> <br>

The problem with above is we have to rollback for all if anyone fails. Complex. 

2. <font color="cyan">Two-phase Commit Protocol</font> <br>
A coordinator is introduced to poll all data sources before making the actual commit. 

<img src="/Users/rajat_mac/Documents/SomethingNewDaily/images/transaction2.png"> <br>

- confirms strong consistency but time taking. 
- single point of failure - coordinator.

3. <font color="cyan">Eventual consistency</font> <br>
assumes idempotence of the data sources and introduces a even processing queue to retain the data until applied to the data sources. retries if fails. 

<img src="/Users/rajat_mac/Documents/SomethingNewDaily/images/transaction3.png"> <br>

***
