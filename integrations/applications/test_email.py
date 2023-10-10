import unittest
from integrations.base_test import BaseTest
from utils.config import generate_random_db_name, get_value_from_json_env_var


class TestEmailConnection(BaseTest):
    """
    Test class for testing the Email datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new Email Datasource.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("email_datasource")
            email_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'email')
            query = self.query_generator.create_database_query(
                        random_db_name,
                        "email",
                        email_config
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Slack", "clmevy37q2171bloee8y2pu2j")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
