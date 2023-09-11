import unittest
from integrations.base_test import BaseTest
from utils.query_generator import QueryGenerator as query
from utils.config import get_value_from_json_env_var, generate_random_db_name

class TestSnowflakeConnection(BaseTest):
    """
    Test class for testing the Snowflake datasource using MindsDB SQL API
    """

    def test_execute_query(self):
        """
        Create new Snowflake datasource
        TODO: This tests will fail when params are missing. It doesn't check if for e.g correct user/pass are used
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("snowflake_datasource")
            snowflake_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'snowflake')
            query = self.query_generator.create_database_query(
                        random_db_name,
                        "snowflake",
                        snowflake_config
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Snowflake", "clgaunphy1301750nd1fvobnz9")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)



if __name__ == "__main__":
    unittest.main()
