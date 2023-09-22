import unittest
from integrations.base_test import BaseTest
from utils.config import generate_random_db_name, get_value_from_json_env_var


class TestStripeConnection(BaseTest):
    """
    Test class for testing the Stripe datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new Stripe Datasource.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("stripe_datasource")
            stripe_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'stripe')
            query = self.query_generator.create_database_query(
                random_db_name,
                "stripe",
                stripe_config
            )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Stripe", "clmq7mgz856085bjopr2mn8g8e")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()