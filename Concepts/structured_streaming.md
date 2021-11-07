## Spark Structured Streaming <br>

1. Use `df.isStreaming` to check if a df is streaming or not.

2. Structured Streaming used micro-batch model to periodically fetch data and use the DataFrame abstraction to represent fetched data. 

3. `spark.readStream` creates an instance of DataStreamReader and `spark.writeStream` creates an instance of DataStreamWriter. A streaming query is created when pipeline starts ( <font color="orange">DataStreamWriter.start</font> method ).

4. **Streaming Joins** <br>
- Joins of streaming query and a batch query are stateless. Joins of 2 streaming queries are stateful. 
