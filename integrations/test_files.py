import unittest
from integrations.base_test import BaseTest
from utils.config import get_value_from_json_env_var


class TestFilesConnection(BaseTest):
    """
    Test class for testing the Files datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Run a simple SELECT query on an uploaded file.
        """
        try:
            cursor = self.connection.cursor()
            files_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'files')
            query = self.query_generator.simple_select_query(
                f"files.{files_config['table_name']}",
            )
            cursor.execute(query)
            cursor.fetchall()
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Files", "clmq7ifa058152bcopwvi1w23o")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)



if __name__ == "__main__":
    unittest.main()
