import unittest
from integrations.base_test import BaseTest
from utils.config import get_value_from_json_env_var, generate_random_db_name


class TestChromaDBConnection(BaseTest):
    """
    Test class for testing the ChromaDB datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new ChromaDB Datasource.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("chromadb_datasource")
            chromadb_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'chromadb')
            query = self.query_generator.create_database_query(
                random_db_name,
                "chromadb",
                chromadb_config
            )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("ChromaDB", "clomq9sol222587bkokhlsaiick")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
