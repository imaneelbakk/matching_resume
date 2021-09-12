import pyspark.sql.types
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql.functions import lower, col,upper
import pandas as pd

spark = SparkSession

# Immutability Example
# Load the CSV file
spark = SparkSession.builder.master("local").appName("data_collection").getOrCreate()

df = spark\
    .read\
    .format("csv")\
    .options(header = 'true', inferSchema = 'true')\
    .option('multiLine', True) \
    .load("./csvFiles/data_collection.csv")

print(f'Record count is: {df.count()}')
df.show()
df = df.dropna(how="any")
print(f'Record count is: {df.count()}')
df.show()

