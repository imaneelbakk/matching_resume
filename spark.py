from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
if __name__ == '__main__':
    scSpark = SparkSession \
        .builder \
        .appName("reading csv") \
        .getOrCreate()
data_file = './csvFiles/data_collection.csv'
sdfData = scSpark.read.csv(data_file, header=True, sep=",").cache()
print('Total Records = {}'.format(sdfData.count()))
sdfData.show()