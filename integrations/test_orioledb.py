import unittest
from integrations.base_test import BaseTest
from utils.config import get_value_from_json_env_var, generate_random_db_name


class TestOrioleDBConnection(BaseTest):
    """
    Test class for testing the OrioleDB datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new OrioleDB Datasource.
        """
        try:
            cursor = self.connection.cursor()
            orioledb_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'orioledb')
            random_db_name = generate_random_db_name("orioledb_datasource")
            query = self.query_generator.create_database_query(
                random_db_name,
                "orioledb",
                orioledb_config
            )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("OrioleDB", "clpqqtfb5119825b3ohe6gck4xs")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
