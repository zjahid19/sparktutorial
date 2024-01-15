# SparkConf is COnfiguration for spark application,Used to set the various Spark parameter in term of key value pairs

from pyspark.conf import SparkConf

# it has two types of methodes 1.setters and 2.getters
spark_configuration = SparkConf()

#setAppName - to set the application name and setMaster - to set the Master URL
spark_configuration.setAppName('First PySpark').setMaster("local")

# get all the parameter which is set earlier
print(spark_configuration.getAll())

