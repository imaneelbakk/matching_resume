
import pyspark.sql.types
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql.functions import lower, col,upper
import pandas as pd
import string
string.punctuation

spark = SparkSession

# Immutability Example
# Load the CSV file
# aa_dfw_df = spark.read.format('csv').options(Header=True).load('./csvFiles/data_collection.csv')

# aa_dfw_df = spark.read.load('./csvFiles/data_collection.csv',

# df = spark.read.format("csv").load("./csvFiles/data_collection.csv")
# df = spark.read.csv('./csvFiles/data_collection.csv', header=False, sep='\t')
spark = SparkSession.builder.master("local").appName("data_collection").getOrCreate()

df = spark\
.read\
.format("csv")\
.options(header = 'true', inferSchema = 'true')\
.option('multiLine', True) \
.load("./csvFiles/data_collection.csv")

def remove_punctuation(text):
    no_punct=[words for words in text if words not in string.punctation]
    words_wo_punct=''.join(no_punct)
    return words_wo_punct
df['Location_wo_punct']=df['Location'].apply(lambda x: remove_punctuation(x))
df.head()
df.show()



print(f'Record count is: {df.count()}')





# # Add the airport column using the F.lower() method
#
# # Drop the Destination Airport column
# aa_dfw_df = aa_dfw_df.drop(aa_dfw_df['Destination Airport'])
#
# # Show the DataFrame
# aa_dfw_df.show()