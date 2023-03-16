from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("k8s://https://127.0.0.1:8001") \
    .appName("Word Count") \
    .config("spark.submit.deployMode","cluster") \
    .config("spark.executor.instances", 5) \
    .config("spark.kubernetes.container.image", "gcr.io/spark/spark:v3.1.1") \
    .config()
    .getOrCreate()

df = spark.sql("select 'spark' as hello")

df.show()
