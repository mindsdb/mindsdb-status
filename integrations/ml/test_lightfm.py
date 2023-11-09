import unittest

from integrations.base_test import BaseTest
from utils.config import generate_random_db_name

class TestLightFMConnection(BaseTest):
    """
    Test class for testing the LightFM ML Engine using the MindsDB SQL API.
    """

    def test_create_lightfm_engine(self):
        """
        Create new LightFM ML Engine.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("lightfm_engine")
            query = self.query_generator.create_ml_engine_query(
                random_db_name,
                "lightfm",
                {}
            )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("LightFM", "clopl6fjy0499bhn56cf113zn")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)

if __name__ == "__main__":
    unittest.main()
