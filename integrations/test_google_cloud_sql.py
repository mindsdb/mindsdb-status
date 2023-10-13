import unittest
from integrations.base_test import BaseTest
from utils.query_generator import QueryGenerator as query
from utils.config import get_value_from_json_env_var, generate_random_db_name

class TestGoogleCloudSql(BaseTest):

    def test_execute_query(self):
        """
        Create a new GoogleCloudSql Datasource.
        """
        try:
            cursor = self.connection.cursor()
            cloudsql_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'google_cloud_sql')
            random_db_name = generate_random_db_name("google_cloud_sql_datasource")
            query = self.query_generator.create_database_query(
                random_db_name,
                "google_cloud_sql",
                cloudsql_config
            )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Cloud_sql", "cln1lv5sj9868931138902c6oi22ecfb01")
            self.incident.report_incident("cl8nll9f7106187ol796984487of1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
