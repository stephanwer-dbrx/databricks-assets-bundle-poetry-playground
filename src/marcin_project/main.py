from pyspark.sql import SparkSession
from marcin_project.functions import filter_taxis


def get_taxis(spark: SparkSession):
  return filter_taxis(spark.read.table("samples.nyctaxi.trips"))

def main():
  spark = SparkSession.builder.getOrCreate()
  get_taxis(spark).show(5)


if __name__ == '__main__':
  main()
