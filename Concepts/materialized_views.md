## Materialized Views

### Situation
Consider opening an app like twitter. It takes fraction of seconds to populate the timeline with hundreds of tweets from your followers/ads ranked in a specifc order. Is it really that fast in computing aggregation and joins on a database of millions? **No.** 
They precompute your it all in background. Materialized views are pre-aggregated read optimized version of source data (written to disk in form of regular table)

> SELECT MATERIALIZED VIEW timeline as (SELECT ......);

- Normal views are just aliases to complex queries. All the results and computation is done on the fly and there is no cached result. 

***

### Synchronising Materliazed Views
This can be done in 2 ways:- 

- Periodic full rebuilds <br>
    <font color="orange">self explanatory</font>

- Incremental refreshes <br>
    <font color="orange">more on this later</font>