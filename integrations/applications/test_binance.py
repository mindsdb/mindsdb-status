import unittest
from integrations.base_test import BaseTest
from utils.config import generate_random_db_name, get_value_from_json_env_var


class TestBinanceConnection(BaseTest):
    """
    Test class for testing the Binance datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new Binance Datasource.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("binance_datasource")
            binance_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'binance')
            query = self.query_generator.create_database_query(
                        random_db_name,
                        "binance",
                        binance_config
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Binance", "cll6ifgwl21601bfoj96vvlu0f")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
