import unittest
from integrations.base_test import BaseTest
from utils.query_generator import QueryGenerator as query
from utils.config import get_value_from_json_env_var, generate_random_db_name

class TestAmazonAuroraConnection(BaseTest):
    """
    Test class for testing the Amazon Aurora datasource (for both MySQL and PostgreSQL) using the MindsDB SQL API.
    """

    def test_execute_query_for_mysql(self):
        """
        Create a new Amazon Aurora MySQL Datasource.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("aurora_mysql_datasource")
            aws_mysql_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'aws_mysql')
            query = self.query_generator.create_database_query(
                        random_db_name,
                        "aurora",
                         aws_mysql_config
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Amazon Aurora MySQL", "clktp2ulb175778c1oqbp0rev8j")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)

    def test_execute_query_for_postgresql(self):
        """
        Create a new Amazon Aurora PostgreSQL Datasource.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("aurora_mysql_datasource")
            aws_postgresql_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'aws_postgresql')
            query = self.query_generator.create_database_query(
                        random_db_name,
                        "aurora",
                         aws_postgresql_config
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Amazon Aurora MySQL", "clktp3jrv174405c8oqfjwvunwh")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
