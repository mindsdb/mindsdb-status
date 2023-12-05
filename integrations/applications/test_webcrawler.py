import unittest
from integrations.base_test import BaseTest
from utils.config import generate_random_db_name


class TestWebCrawlerConnection(BaseTest):
    """
    Test class for testing the Web Crawler datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new Web Crawler Datasource.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("web_datasource")
            query = self.query_generator.create_database_query(
                random_db_name,
                "web",
                {}
            )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Web Crawler", "clnx4utjd18018bxlmbabhu1nj")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()