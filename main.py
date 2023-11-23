import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]").appName("NBAAAAA").getOrCreate()
print(spark)
df1 = spark.read.csv("archive/Players.csv")
df2 = spark.read.csv("archive/Seasons_Stats.csv")
df3 = spark.read.csv("archive/player_data.csv")

df1.show()
df2.show()
df3.show()
