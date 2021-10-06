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

1. <font color="cyan">Spark RDD</font> <br>
primary user facing API of Spark. immutable collection of elements distributed across nodes for parallelism to be operated on by low-level APIs. usually schemaless streams of text or something. can be converted to datasets/dataframes.

2. <font color="cyan">Datasets or FataFrames</font> (unified after Spark 2.0) <br>
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

3. <font color="cyan">Repartition</font> <br>
```spark sql
repartition= max(default_parallelism, ceil(ram/target))
```

default parellelism is:
- > (num Executors)X(num ExecutorCores)X(2 or 3)
- target(partition size) is usually 128MB 
- can set ```spark.sql.shuffle.partitions``` based on data size, cores etc. can be se to 1.5 or 2X the initial value of partitions (df.rdd.getnumpartitions). Once any operation is applied to the df, partitions become 200 (default). 

<br>
<img src="/Users/rajat_mac/Documents/SomethingNewDaily/images/repartition.png">


4. <font color="cyan">Spark sorting</font> <br>
How does spark internally achieve sorting?
- samples on the data to computer boundaries for each output partition. (```sample``` followed by ```collect```)
- input rdd is partitioned using rangePartitioner (```repartitionByRange```)
- each partition is sorted internally (```mapPartitions```)


5. <font color="cyan">Serializability in Spark</font> <br>
When you run transformation on rdd (filter, map, flatMap etc.), the following happens:- <br>
    - serlialized on driver node
    - sent to workers
    - deserialized

Suppose we are trying to call a testing function in map as follows <br>

```scala
import org.apache.spark.{SparkContext,SparkConf}

object Spark {
  val ctx = new SparkContext(new SparkConf().setAppName("test").setMaster("local[*]"))
}

object NOTworking extends App {
  new Test().doIT
}

class Test extends java.io.Serializable {
  val rddList = Spark.ctx.parallelize(List(1,2,3))

  def doIT() =  {
    val after = rddList.map(someFunc)
    after.collect().foreach(println)
  }

  def someFunc(a: Int) = a + 1
}
```
Since methods can't be serialized on their own, spark tries to serialize the whole **testing** class. 

> Solution 1:
```scala
import org.apache.spark.{SparkContext,SparkConf}

object Spark {
  val ctx = new SparkContext(new SparkConf().setAppName("test").setMaster("local[*]"))
}

object NOTworking extends App {
  new Test().doIT
}

class Test extends java.io.Serializable {
  val rddList = Spark.ctx.parallelize(List(1,2,3))

  def doIT() =  {
    val after = rddList.map(someFunc)
    after.collect().foreach(println)
  }

  def someFunc(a: Int) = a + 1
}
```
> Solution 2: 
```scala
import org.apache.spark.{SparkContext,SparkConf}

object Spark {
  val ctx = new SparkContext(new SparkConf().setAppName("test").setMaster("local[*]"))
}

object NOTworking extends App {
  new Test().doIT
}

class Test {
  val rddList = Spark.ctx.parallelize(List(1,2,3))

  def doIT() =  {
    val after = rddList.map(someFunc)
    after.collect().foreach(println)
  }

  val someFunc = (a: Int) => a + 1
}
```

6. <font color="cyan">Streaming with Spark</font> <br>

    1. **Spark Streaming** <br>
        - works on top of DStream API (internally used RDDs. 
        - data comes in microbatches based on the trigger interval.

    2. **Structured Streaming** (Spark2.x ONWARDS) <br>
        - no batches, data appended to continuous flowing stream.
        - built on top of DataFrames/Dataset API so sql queries/scala function to process data can be applied on top.
        -  each row processed and appended to unounded result table based on usecase (update/append etc.)


7. 