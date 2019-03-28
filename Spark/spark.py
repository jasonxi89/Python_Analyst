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
