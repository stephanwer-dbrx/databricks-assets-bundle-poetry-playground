# This is an example of a unit test with spark running in local mode

from marcin_project import functions
from chispa.dataframe_comparer import *
from pyspark.sql import SparkSession

# If you don't want to use pytest-spark then define spark session as below:
#spark_session = SparkSession.builder.getOrCreate()

def test_get_taxi(spark_session: SparkSession): # using pytest-spark
    schema = "trip_distance: double, fare_amount: double"
    test_df = spark_session.createDataFrame([[1.0, 1.0], [1.2, 6.0]], schema)
    expected_df = spark_session.createDataFrame([[1.2, 6.0]], schema)

    actual_df = functions.filter_taxis(test_df)

    assert_df_equality(actual_df, expected_df)
