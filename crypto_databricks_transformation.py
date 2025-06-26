# Databricks notebook source
# MAGIC %md
# MAGIC ###  Incoming Json message
# MAGIC {
# MAGIC   "date": "2024-07-01 00:00:00",
# MAGIC   "price": 62734.39
# MAGIC }

# COMMAND ----------

EVENT_HUB_CONN_STR = dbutils.secrets.get(scope="my-scope", key="EVENT_HUB_CONN_STR")

# COMMAND ----------

ehConf = {
  'eventhubs.connectionString': dbutils.secrets.get(scope="my-scope", key="EVENT_HUB_CONN_STR"),
  'eventhubs.consumerGroup': '$Default'
}

df_raw = (
    spark.readStream
    .format("eventhubs")
    .options(**ehConf)
    .load()
)

from pyspark.sql.types import StructType, StringType, DoubleType

schema = StructType() \
    .add("date", StringType()) \
    .add("price", DoubleType())

from pyspark.sql.functions import from_json, col

df_parsed = df_raw \
    .selectExpr("CAST(body AS STRING) AS json_str") \
    .select(from_json(col("json_str"), schema).alias("data")) \
    .select("data.*") \
    .withColumn("date", col("date").cast("timestamp"))


# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import lag, round, avg

df_parsed.createOrReplaceTempView("crypto_stream_temp")


# COMMAND ----------

SELECT
  date,
  price,
  ROUND(100 * (price - LAG(price) OVER (ORDER BY date)) / LAG(price) OVER (ORDER BY date), 2) AS percent_change,
  ROUND(AVG(price) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS moving_avg_7
FROM crypto_stream_temp


# COMMAND ----------

output_path = "/mnt/delta/crypto_analysis"
checkpoint_path = "/mnt/delta/crypto_checkpoints"

query = transformed_df.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", checkpoint_path) \
    .start(output_path)
