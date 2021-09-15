## Bucketing

- Within partitions, basically subgroups of files (more even in sizes the better). can be specified with the clusteredy by (```user_id```) into X buckets clause. 
- E.g. users logging per country: Partition of US will be much bigger than New Zealand so can be solved by bucketing on some attribute that is mostly unique. 

***

## Bloom Filters

- Mostly used when joining large tables or many queries on some table with = operator. 
- A bloom filter is a hash value for data in a column in a given block of data. Thus, can ask a bloom filter if a given block contains a value ```Country= US``` or ```Gender=female```.
- Currently only work with the ORC table format in hive.

***

## Predicate Pushdown

- Allows **where** to be executed before the join resulting in less data sent over the network.
> set hive.optimize.ppd=true;


