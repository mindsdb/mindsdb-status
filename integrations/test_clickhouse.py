import unittest
from integrations.base_test import BaseTest
from utils.query_generator import QueryGenerator as query
from utils.config import get_value_from_json_env_var, generate_random_db_name


class TestClickHouseConnection(BaseTest):
    """
    Test class for testing the ClickHouse datasource using MindsDB SQL API
    """

    def test_execute_query(self):
        """
        Create new ClickHouse Datasource
        """
        try:
            cursor = self.connection.cursor()
            clickhouse_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'clickhouse')
            random_db_name = generate_random_db_name("clickhouse_datasource")
            query = self.query_generator.create_database_query(
                        random_db_name,
                        "clickhouse",
                         clickhouse_config
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("ClickHouse", "clgaunv4w1297557nd5qdvodyo")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
