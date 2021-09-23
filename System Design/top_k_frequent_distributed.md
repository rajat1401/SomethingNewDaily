## Find top-k frequent elements

- count of elements beyond capacity of single machine
- real-time stream incoming

**Solution** <br>
streaming mapreduce. <br>
1. clients send elements to ```load balancer``` connected to the ```mappers```.
2. don't want to send distinct elements to each reducer and keep millions of counts so partition the element space. 
3. each element space can be one kafka topic and reducers subscribe to it. 
4. what if need to add or remove topics? - <font color="orange">Consistent Hashing of topics</font>. <br>
<br>

<img src="/Users/rajat_mac/Documents/SomethingNewDaily/images/topk.png">

OP.

***