import unittest
from utils.query_generator import QueryGenerator as query
from utils.config import generate_random_db_name
from integrations.base_test import BaseTest
from utils.config import  get_value_from_json_env_var, generate_random_db_name

class TestAnthropicConnection(BaseTest):
    """
    Test class for testing the Anthropic ML Engine using the MindsDB SQL API.
    """

    def test_create_anthropic_engine(self):
        """
        Create new Anthropic ML Engine.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("anthropic_engine")
            anthropic_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'anthropic')
            query = self.query_generator.create_ml_engine_query(
                        random_db_name,
                        "anthropic",
                        anthropic_config
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Anthropic", "clktqxt8o55593bxohrv6fcswq")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)

if __name__ == "__main__":
    unittest.main()