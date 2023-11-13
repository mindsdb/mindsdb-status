import unittest

from integrations.base_test import BaseTest
from utils.config import get_value_from_json_env_var, generate_random_db_name

class TestCohereConnection(BaseTest):
    """
    Test class for testing the Cohere ML Engine using the MindsDB SQL API.
    """

    def test_create_cohere_engine(self):
        """
        Create new Cohere ML Engine.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("cohere_engine")
            cohere_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'cohere')
            query = self.query_generator.create_ml_engine_query(
                random_db_name,
                "cohere",
                cohere_config
            )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Cohere", "clor6i4bi8704bkn4pvdfai6p")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)

if __name__ == "__main__":
    unittest.main()
