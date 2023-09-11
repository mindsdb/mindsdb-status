import unittest
from integrations.base_test import BaseTest
from utils.config import generate_random_db_name, get_value_from_json_env_var


class TestYouTubeConnection(BaseTest):
    """
    Test class for testing the YouTube datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new YouTube Datasource.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("youtube_datasource")
            youtube_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'youtube')
            query = self.query_generator.create_database_query(
                        random_db_name,
                        "youtube",
                        youtube_config
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("YouTube", "clkwhx4626787btna7vrreal6")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
