import unittest
from utils.config import generate_random_db_name
from integrations.base_test import BaseTest


class TestTimeGPTConnection(BaseTest):
    """
    Test class for testing the TimeGPT ML Engine using the MindsDB SQL API.
    """

    def test_create_timegpt_engine(self):
        """
        Create new TimeGPT ML Engine.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("timegpt_engine")
            query = self.query_generator.create_ml_engine_query(
                        random_db_name,
                        "timegpt",
                        {}
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Nixtla's TimeGPT", "clmj4dcp768369c7n5vfqriv5r")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
