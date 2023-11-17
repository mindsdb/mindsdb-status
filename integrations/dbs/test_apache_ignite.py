import unittest
from integrations.base_test import BaseTest
from utils.query_generator import QueryGenerator as query
from utils.config import get_value_from_json_env_var, generate_random_db_name


class TestApacheIgniteConnection(BaseTest):
    """
    Test class for testing the Apache Ignite datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new Apache Ignite Datasource.
        """
        try:
            cursor = self.connection.cursor()
            apache_ignite_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'apache_ignite')
            random_db_name = generate_random_db_name("apache_ignite_datasource")
            query = self.query_generator.create_database_query(
                        random_db_name,
                        "ignite",
                         apache_ignite_config
            )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Apache Ignite", "cll41e2to1892b7o8xquc22d2")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
