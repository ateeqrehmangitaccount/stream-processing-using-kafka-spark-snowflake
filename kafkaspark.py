from os import truncate
from select import select

from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructField,StructType, StringType, IntegerType
import pandas as pd


conf=SparkConf() \
    .set('spark.jars.packages','org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.2')

spark = SparkSession.builder.appName('testspark').config(conf=conf).getOrCreate()

df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("subscribe", "firsttopic") \
  .option("includeHeaders", "true") \
  .load()


result=df.selectExpr("CAST(value as string)") \
    .writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("topic", "secondtopic") \
    .option("checkpointLocation", "/home/marehman/output/") \
    .start()


result.awaitTermination()

