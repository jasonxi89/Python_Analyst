# # from pyspark import SparkConf, SparkContext
# #
# # #创建sparkconf:设置spark的相关信息
# # con = SparkConf().setMaster("local[2]").setAppName("spark0325")
# #
# # #创建sparkcontext
# # sc = SparkContext(conf = con)
# #
# # #业务逻辑
# # data = [i for i in range(1,6)]
# # disData = sc.parallelize(data)
# # print(disData.collect())
# #
# #
# # sc.stop()
# #
# #
# from pyspark.sql import SparkSession
#
# data = [('a',5),('b',7),('c',6),('d',1)]
# print(sorted(data,key=lambda x:x[1],reverse=True))
#
# spark = SparkSession.builder.appName("spark0801").getOrCreate()
# spark.stop()
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == '__main__':
    sc = SparkContext(appName="spark0901")
    ssc = StreamingContext(sc, 5)

    #TODO....根据业务需求开发自己的业务

    #Define the input sources by creating input DStreams.
    lines = ssc.socketTextStream("",9999)

    # Define the streaming computations by applying transformation
    counts = lines.flatMap(lambda line:line.split(" "))\
                .map(lambda word:(word, 1))\
                .reduceByKey(lambda x,y: x + y)

    #output operation to Dstreams
    counts.pprint()

    #Start receiving data and processing it using streamingContext.start().
    ssc.start()

    #Wait for the processing to be stopped (manually or due to any error) using streamingContext.awaitTermination().
    ssc.awaitTermination()