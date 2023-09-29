import unittest
from integrations.base_test import BaseTest
from utils.config import get_value_from_json_env_var, generate_random_db_name


class OceanBaseConnection(BaseTest):
    """
    Test class for testing the OceanBase datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new OceanBase Datasource.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("oceanbase_datasource")
            oceanbase_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'oceanbase')
            query = self.query_generator.create_database_query(
                random_db_name,
                "oceanbase",
                oceanbase_config
            )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("OceanBase", "cln1kmzmy130779bbmzwsz7yepe")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
