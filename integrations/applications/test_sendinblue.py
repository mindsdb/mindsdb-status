import unittest
from integrations.base_test import BaseTest
from utils.config import generate_random_db_name, get_value_from_json_env_var


class TestSendinblueConnection(BaseTest):
    """
    Test class for testing the Sendinblue datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new Sendinblue Datasource.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("sendinblue_datasource")
            sendinblue_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'sendinblue')
            query = self.query_generator.create_database_query(
                random_db_name,
                "sendinblue",
                sendinblue_config
            )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Sendinblue", "clmuixlbt491406axoc392n13ps")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
