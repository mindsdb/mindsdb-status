import unittest
import mysql.connector
from utils.query_generator import QueryGenerator as query
from utils.config import MYSQL_API_CONFIG, SINGLESTORE_CONFIG, generate_random_db_name
from utils.log import setup_logger


class TestSingleStoreConnection(unittest.TestCase):
    """
    Test class for testing the SingleStore datasource using MindsDB SQL API
    """

    def setUp(self):
        """
        Set up the test environment by establishing a connection
        to the MindsDB SQL API.
        """
        self.query_generator = query()
        self.logger = setup_logger(__name__)
        try:
            self.connection = mysql.connector.connect(**MYSQL_API_CONFIG)
        except mysql.connector.Error as err:
            self.logger.error('Connection to SQL API Failed')
            self.logger.exception(err)

    def tearDown(self):
        """
        Clean up the test environment by closing the connection
        to the MindsDB SQL API.
        """
        if self.connection.is_connected():
            self.connection.close()

    def test_connection_established(self):
        """
        Test that the connection to the MindsDB SQL API is established
        """
        assert self.connection.is_connected()

    def test_execute_query(self):
        """
        Create new SingleStore Datasource
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("singlestore_datasource")
            query = self.query_generator.create_database_query(
                        random_db_name,
                        "singlestore",
                         SINGLESTORE_CONFIG
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            self.logger.exception(err)
            assert False, f"Error executing query: {err}"


if __name__ == "__main__":
    unittest.main()
