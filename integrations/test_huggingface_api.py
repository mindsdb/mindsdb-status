import unittest
import mysql.connector
from utils.query_generator import QueryGenerator as query
from utils.config import MYSQL_API_CONFIG, HUGGINGFACE_API_CONFIG, generate_random_db_name
from utils.log import setup_logger


class TestHuggingFaceAPIConnection(unittest.TestCase):
    """
    Test class for testing the HuggingFace API ML Engine using the MindsDB SQL API.
    """

    def setUp(self):
        """
        Set up the test environment by establishing a connection to the MindsDB SQL API.
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
        Clean up the test environment by closing the connection.
        to the MindsDB SQL API.
        """
        if self.connection.is_connected():
            self.connection.close()

    def test_connection_established(self):
        """
        Test that the connection to the MindsDB SQL API is established.
        """
        assert self.connection.is_connected()