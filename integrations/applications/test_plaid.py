import unittest
from integrations.base_test import BaseTest
from utils.query_generator import QueryGenerator as query
from utils.config import get_value_from_json_env_var, generate_random_db_name


class TestPlaidConnection(BaseTest):
    """
    Test class for testing the Plaid datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new Plaid Datasource.
        """
        try:
            cursor = self.connection.cursor()
            plaid_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'plaid')
            random_db_name = generate_random_db_name("plaid_datasource")
            query = self.query_generator.create_database_query(
                        random_db_name,
                        "plaid",
                         plaid_config
            )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Plaid", "cln1lv5s33578668j317552715432c6oi22ecfb01")
            self.incident.report_incident("cl8nll9f7106187o455478790lo45523f1968m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
