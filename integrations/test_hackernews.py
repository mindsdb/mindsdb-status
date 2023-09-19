import unittest
from integrations.base_test import BaseTest
from utils.config import generate_random_db_name


class TestHackerNewsConnection(BaseTest):
    """
    Test class for testing the Hacker News datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new Hacker News Datasource.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("hackernews_datasource")
            query = self.query_generator.create_database_query(
                random_db_name,
                "hackernews",
                {}
            )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Hacker News", "clmq7mgz856085bjopr2mn8g8e")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
