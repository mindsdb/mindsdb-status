import unittest
from integrations.base_test import BaseTest
from utils.config import generate_random_db_name, get_value_from_json_env_var


class TestGitHubConnection(BaseTest):
    """
    Test class for testing the GitHub datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new GitHub Datasource.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("github_datasource")
            github_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'github')
            query = self.query_generator.create_database_query(
                        random_db_name,
                        "github",
                         github_config
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("GitHub", "clkwi384m10871bmnayp9s5a5s")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
