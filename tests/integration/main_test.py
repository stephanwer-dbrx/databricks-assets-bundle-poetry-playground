# This is an example of an integration tests that leverages Databricks Connect

from databricks.connect import DatabricksSession
from marcin_project import main

# This will create a new Databricks Connect session. If this fails,
# check that you have configured Databricks Connect correctly.
# See https://docs.databricks.com/dev-tools/databricks-connect.html
# Check limitations: https://docs.databricks.com/en/dev-tools/databricks-connect-legacy.html#limitations
# For the test to work the provided cluster must be in running state.

# This will take auth details from the DEFAULT profile from .databrikcscfg file:
# https://docs.databricks.com/dev-tools/databricks-connect-ref.html#requirements
spark = DatabricksSession.builder.getOrCreate()
# You can also provide auth credentials using .sdkConfig(config)

# Build explicitly
# spark = DatabricksSession.builder.remote(
#    host=f"XXX",
#    token="xxx",
#    cluster_id="xxx"
# ).getOrCreate()

def test_main():
    taxis = main.get_taxis(spark)
    assert taxis.count() > 5
