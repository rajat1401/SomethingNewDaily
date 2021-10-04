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