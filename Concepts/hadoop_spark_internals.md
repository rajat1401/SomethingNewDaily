## Hadoop

Distributed storage and computation of v. large datasets. mainly 3 components:- 

1. **hdfs** <br>
underlying fs of hadoop cluster. scalable, fault-tolerant and rack-aware. data -> blocks -> dist across cluster. (default blocks 128MB)

    - NameNode <br>
    manages fs namespace, file-block mapping (meta-data) and brokers access to files. operates in memory persists state to disk. stores all metadata in fs image and edit log.

    - Secondary Namenode (Optional) <br>
    has own fs image that updates independently when change made to edit log so if main namenode goes down, don't have to replay millions of actions from edit log.


2. **map-reduce** <br>
framework that processes data in distributed fashion. 

3. **YARN** <br>
handles resource allocation to mr jobs. main 3 components. 

    - resource manager <br>
    rack aware leader keeps track of resources and runs the scheduler w/c allocates resources to running applications by assigning containers to requesting application masters
    - application master <br>
    each applicaiton has a master. heartbeat sent here/ask for extra resources then this asks to scheduler. masters run on their own node.

4. **Zookeeper** <br>
now decoupled with YARN. used for high availability of pts. of failure like YARN resource manager / hdfs namenode etc. 

***

## Spark

Basically a driver and cluster manager (yarn/mesos/standalone) that allocates resources across applications. driver creates sparkcontext, acquires executors on nodes in the cluster and sends code (JAR) to executors. sparkcontext sends tasks to executors (after DAG is made). 

spark sql -> catalyst optimizer -> logocal plan -> physical plan -> DAG

1. Spark RDD's <br>
primary user facing API of Spark. immutable collection of elements distributed across nodes for parallelism to be operated on by low-level APIs. usually schemaless streams of text or something. can be converted to datasets/dataframes.

2. Datasets or FataFramses ( <font color="orange">unified after Spark 2.0</font> ) <br>
also immutable distruted collection of data but with a schema. unified to a single high-level API:- <br>

    - Dataset[Row] (untyped - DataFrames)
    - Dataset[T] (type-safe - Datasets) 

**Advantages of Datasets/DataFrames**
- Space efficient to RDDs
- Performance optimization in catalyst optimizer
- Static typing and runtime type-safety

```spark sql
val ds = spark.read.json(“/databricks-public-datasets/data/iot/iot_devices.json”).as[DeviceIoTData]
```
works, given you have a case-class names ```DeviceIoTData```.
 