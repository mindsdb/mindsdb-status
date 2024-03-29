import unittest
from integrations.base_test import BaseTest
from utils.config import generate_random_db_name, get_value_from_json_env_var


class TestPayPalConnection(BaseTest):
    """
    Test class for testing the PayPal datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new PayPal Datasource.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("paypal_datasource")
            paypal_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'paypal')
            query = self.query_generator.create_database_query(
                random_db_name,
                "paypal",
                paypal_config
            )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("PayPal", "clpqqhs51112000b3ohx5a6766t")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
