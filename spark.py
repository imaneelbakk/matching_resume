import pyspark.sql.types
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql.functions import lit, lower, col,upper
import pandas as pd
import re
from pyspark.sql.functions import regexp_replace, trim, col, lower
from pyspark.sql.functions import when
from pyspark.sql.functions import monotonically_increasing_id 
import functools
import pandas
from pyspark.ml.feature import RegexTokenizer

# Load the CSV file
spark = SparkSession.builder.master("local").appName("data_collection").getOrCreate()
mySchema = StructType([ StructField("Title", StringType(), True)\
                    ,StructField("Company", StringType(), True)\
                    ,StructField("Location", StringType(), True)\
                    ,StructField("Experience", StringType(), True)\
                    ,StructField("Studies-level", StringType(), True)\
                    ,StructField("Domain", StringType(), True)\
                    ,StructField("Requirements", StringType(), True)\
                    ,StructField("Contract", StringType(), True)\
                    ,StructField("Links", StringType(), True)\
                    ,StructField("Date", DateType(), True)])
df = spark\
    .read\
    .format("csv")\
    .options(header = 'true')\
    .option('multiLine', True) \
    .load("./csvFiles/data_collection.csv")

df_index = df.select("*").withColumn("id", monotonically_increasing_id())



def removePunctuation(column,alias):
    return trim(lower(regexp_replace(column, '[^A-Za-z0-9 ]', ''))).alias(alias)
def removePunctuationNumbers(column,alias):
    return trim(lower(regexp_replace(column, '[^A-Za-z ]', ''))).alias(alias)
def getColumn(column,alias):
    return trim(lower(column)).alias(alias)

df1=df_index.select(removePunctuationNumbers(col('Requirements'),'RequirementsClean'))
df1_index = df1.select("*").withColumn("index", monotonically_increasing_id())

df2=df.select(removePunctuationNumbers(col('Title'),'TitleClean'))
df2_index = df2.select("*").withColumn("index", monotonically_increasing_id())

df3=df_index.select(removePunctuation(col('Company'),'CompanyClean'))
df3_index = df3.select("*").withColumn("index", monotonically_increasing_id())

df4=df.select(removePunctuation(col('Location'),'LocationClean'))
df4_index = df4.select("*").withColumn("index", monotonically_increasing_id())

df5=df_index.select(removePunctuationNumbers(col('Domain'),'DomainClean'))
df5_index = df5.select("*").withColumn("index", monotonically_increasing_id())

df6=df_index.select(removePunctuation(col('Experience'),'ExperienceClean'))
df6_index = df6.select("*").withColumn("index", monotonically_increasing_id())

df7=df_index.select(removePunctuation(col('Studies-level'),'StudiesLevelClean'))
df7_index = df7.select("*").withColumn("index", monotonically_increasing_id())

df8=df_index.select(removePunctuationNumbers(col('Contract'),'ContractClean'))
df8_index = df8.select("*").withColumn("index", monotonically_increasing_id())

df9=df_index.select(getColumn(col('Links'),'LinksClean'))
df9_index = df9.select("*").withColumn("index", monotonically_increasing_id())

df10=df_index.select(getColumn(col('Date'),'DateClean'))
df10_index = df10.select("*").withColumn("index", monotonically_increasing_id())

def unionFunction(df1_index,df2_index):
    return df1_index.join(df2_index,"index")



newone1 = unionFunction(df1_index,df2_index)
newone2 = unionFunction(newone1,df3_index)
newone3 = unionFunction(newone2,df4_index)
newone4 = unionFunction(newone3,df5_index)
newone5 = unionFunction(newone4,df6_index)
newone6 = unionFunction(newone5,df7_index)
newone7 = unionFunction(newone6,df8_index)
newone8 = unionFunction(newone7,df9_index)
DF_index = unionFunction(newone8,df10_index)

# DF_index= DF_index.select("*").toPandas()

# for column in DF_index[["TitleClean","DomainClean","RequirementsClean","ContractClean"]]:
#     DF_index[column] = DF_index[column].str.replace('\d+', '')

# main = spark.createDataFrame(DF_index)
DF_index.show()
#print(DF_index.head(90))