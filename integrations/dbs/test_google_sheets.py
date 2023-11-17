import unittest
from integrations.base_test import BaseTest
from utils.query_generator import QueryGenerator as query
from utils.config import get_value_from_json_env_var, generate_random_db_name


class TestGoogleSheetsConnection(BaseTest):
    """
    Test class for testing the Google Sheets datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new Google Sheets Datasource.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("google_sheets_datasource")
            sheet_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'google_sheet')
            query = self.query_generator.create_database_query(
                        random_db_name,
                        "sheets",
                         sheet_config
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Google Sheet", "cllf7xuyp10564chol6kaf1qp1")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)



if __name__ == "__main__":
    unittest.main()
