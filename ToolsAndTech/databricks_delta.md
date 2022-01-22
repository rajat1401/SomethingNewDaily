## Databrics Delta tables

1. <font color="orange">Change data capture</font> <br>
    Common usecase is to perform CDC(insert/update/delete) from one or many datasources into delta table(s). source could be:- <br>
        - ETL tool like oracle GoldenGate
        - Kafka
        - Spark structured streaming

    The tables can be refreshed at daily/hourly/15-min basis. 
    Current pipeline: GG -> S3(parquet?) -> Spark Job -> Delta. For streaming cases, Kafka -> Spark -> Delta. 

    Can maintain a spark job such that for every refresh period, `insert into staging table and insert overwrite current version of recordset from staging to final/snapshot table.` <br>
    [Link](https://databricks.com/blog/2018/10/29/simplifying-change-data-capture-with-databricks-delta.html)
    
    <br>
    

2. 

