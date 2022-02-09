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
    

2. <font color="orange">Data Migration Delta to Athena/Presto</font> (for analysis) <br>
    Generate symlink manifest file for the delta table which tells which files to read in the data when running a query instead of doing a complete data listing. <br>
    > GENERATE symlink_format_manifest FOR TABLE DELTA.<path_to_table> <br>
    
    Can also define property `delta.compatibility.symlinkFormatManifest.enabled=true` for auto-updation of manifest file upon CDC. 

    Define an external table in Presto/Athena as follows:- <br>
    ```sql
        CREATE EXTERNAL TABLE mytable (name string) PARTITIONED BY (date_part date) ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.SymlinkTextInputFormat'OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'LOCATION '<path-to-delta-table>/_symlink_format_manifest/'
    ```
    [Link](https://docs.databricks.com/delta/presto-integration.html)
    
    <br>


3. <font color="orange">Optimize</font> <br>
    Optimize entire table, subset of data (using `where`) or colocate data by a column (using `zorder`). If no colocation specified, bin packing optimization is performed. <br>
    1. Bin packing opt. is idempotent. produces evenly balanced data files. 
    2. Z-ordering not idempotent but if no new data added to a partition, another z-ordering will have no effect. 

    ```sql
    OPTIMIZE events WHERE date >= '2017-01-01'

    OPTIMIZE events WHERE date >= current_timestamp() - INTERVAL 1 day ZORDER BY (eventType)
    ```
    [Link](https://docs.databricks.com/spark/latest/spark-sql/language-manual/delta-optimize.html)

    <br>


4. 



