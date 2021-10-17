## Spark Functions

1. ```collect_list()``` <br>
    - unifies values into an array. 
    - maintains order. 
    - doesn't remove duplicates.

<img src="/Users/rajat_mac/Documents/SomethingNewDaily/images/collect_list.png">

```spark sql
val collect_list_df = array_dataframe.groupBy("name").agg(collect_list("toolSet").as("toolSet"))
```
**output**: <br>

<img src="/Users/rajat_mac/Documents/SomethingNewDaily/images/collect_list2.png">

> to remove duplicates, use array_distinct


2. ```collect_set()``` <br>
    - eliminates duplicates.
    - doesn't maintain order.


3. ```string To date``` <br>

    By default, spark converts string to data when reading with inferSceham. use <font color="cyan">withColumn</font> and <font color="cyan">to_date</font> to deal with it. 

    <img src="/Users/rajat_mac/Documents/SomethingNewDaily/images/withcolumn.png"> <br>


4. ```groupBy``` and ```agg``` <br>

    groupBy created a RotationalDataset rathet than a df. use agg with it for count/sum/max along with ```alias``` to create new aggregations and result is a df. 

    > <font color="cyan">alias</font> also helpful in joining dataframes. 
    
    <img src="<image here for join"> <br>


5. ```Window``` and ```rank/row_number/dense_rank```

    Learn this syntax.

    <img src="image here"> 
