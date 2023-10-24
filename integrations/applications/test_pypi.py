import unittest
from integrations.base_test import BaseTest
from utils.config import generate_random_db_name


class TestPyPIConnection(BaseTest):
    """
    Test class for testing the PyPI datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new PyPI Datasource.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("pypi_datasource")
            query = self.query_generator.create_database_query(
                random_db_name,
                "pypi",
                {}
            )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("PyPI", "clmt4gm0n12728b8n3e6nkz55p")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
