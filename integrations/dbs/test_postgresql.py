import unittest
from integrations.base_test import BaseTest
from utils.query_generator import QueryGenerator as query
from utils.config import get_value_from_json_env_var, generate_random_db_name

class TestPostgreSQLConnection(BaseTest):
    """
    Test class for testing the PostgreSQL datasource using MindsDB SQL API
    """

    def test_execute_query(self):
        """
        Create new PostgreSQL Datasource
        """
        try:
            cursor = self.connection.cursor()
            psql_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'postgresql')
            random_db_name = generate_random_db_name("postgresql_datasource")
            query = self.query_generator.create_database_query(
                        random_db_name,
                        "postgres",
                         psql_config
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("PostgreSQL", "clg3ro9pj59766bdoia5mkdgdb")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
