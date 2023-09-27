import unittest
from integrations.base_test import BaseTest
from utils.query_generator import QueryGenerator as query
from utils.config import get_value_from_json_env_var, generate_random_db_name


class TestAstraDBConnection(BaseTest):
    """
    Test class for testing the Datastax AstraDB datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new AstraDB Datasource.
        """
        try:
            cursor = self.connection.cursor()
            astra_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'astradb')
            random_db_name = generate_random_db_name("astra_datasource")
            query = self.query_generator.create_database_query(
                        random_db_name,
                        "astra",
                         astra_config
            )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Datastax AstraDB", "cln1lv5sj31132c6oi22ecfb01")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
