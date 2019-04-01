from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import *


def get_grade(value):
    if 0 <= value <= 50:
        return "Great"
    elif value <= 100:
        return "Normal"
    elif value <= 150:
        return "Not health for children"
    elif value <= 200:
        return "Not health"
    elif value <= 300:
        return "Very bad"
    elif value <= 500:
        return "dangerous"
    elif value > 500:
        return "LEAVE NOW"
    else:
        return None



if __name__ == '__main__':
    spark = SparkSession.builder.appName("Air Analyst").getOrCreate()

    #option("header","true")最上面一行为header,option("inferSchema","true")根据信息值判断信息类型
    df = spark.read.format("csv")\
        .option("header","true")\
        .option("inferSchema","true")\
        .load("file:///Users/xi/Downloads/Beijing_2008_HourlyPM2.5_created20140325.csv")\
        .select("Year","Month","Day","hour","Value","Qc name")


    #增加单元格，要制定单元格的类型，就和写sql一样，所以要先处理下类型
    grade_function_udf = udf(get_grade,StringType())
    #进来一个Value,返回一个grade,并且用grade新增一行
    df.withColumn("Grade",grade_function_udf(df['Value']))

    spark.stop()
