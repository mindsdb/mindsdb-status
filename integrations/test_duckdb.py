import unittest
from integrations.base_test import BaseTest
from utils.query_generator import QueryGenerator as query
from utils.config import get_value_from_json_env_var, generate_random_db_name

class TestDuckDBConnection(BaseTest):
    """
    Test class for testing the DuckDB datasource using MindsDB SQL API
    """

    def test_execute_query(self):
        """
        Create new DuckDB Datasource
        """
        try:
            cursor = self.connection.cursor()
            duckdb_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'duckdb')
            random_db_name = generate_random_db_name("duckdb_datasource")
            query = self.query_generator.create_database_query(
                        random_db_name,
                        "duckdb",
                         duckdb_config
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("DuckDB", "cll2bthzp11419bjol5mjiu1ln")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()