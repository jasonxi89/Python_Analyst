from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.appName("Air Analyst").getOrCreate()

    df = spark.read.format("csv").load("file://Users/xi/Downloads/Beijing_2008_HourlyPM2.5_created20140325.csv")
    