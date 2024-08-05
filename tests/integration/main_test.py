# this test uses Databricks Connect

from databricks.connect import DatabricksSession
from marcin_project import main

# This will create a new Databricks Connect session. If this fails,
# check that you have configured Databricks Connect correctly.
# See https://docs.databricks.com/dev-tools/databricks-connect.html

# Take connection from .databrikcscfg file, DEFAULT profile
# https://docs.databricks.com/dev-tools/databricks-connect-ref.html#requirements
spark = DatabricksSession.builder.getOrCreate()
# provide profile optionally: .profile("profile_name")
# or config via sdkConfig(config) with various auth option

# Build explicitly
# spark = DatabricksSession.builder.remote(
#    host=f"XXX",
#    token="xxx",
#    cluster_id="xxx"
# ).getOrCreate()

def test_main():
    taxis = main.get_taxis(spark)
    assert taxis.count() > 5
