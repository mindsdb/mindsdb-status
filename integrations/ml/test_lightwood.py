import unittest
from utils.config import generate_random_db_name
from integrations.base_test import BaseTest


class TestLightwoodConnection(BaseTest):
    """
    Test class for testing the Lightwood ML Engine using the MindsDB SQL API.
    """

    def test_create_Lightwood_engine(self):
        """
        Create new Lightwood ML Engine.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("lightwood_engine")
            query = self.query_generator.create_ml_engine_query(
                        random_db_name,
                        "lightwood",
                        {}
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("MindsDB's Lightwood", "clmj5ha4t93628c7n5ghp3v7le")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
