import unittest
import mysql.connector
from mysql.connector import errorcode
from utils.query_generator import QueryGenerator as query
from utils.config import get_value_from_json_env_var, generate_random_db_name
from utils.log import setup_logger
from utils.instatus import InstatusClient as ins
from utils.template import IncidentTemplate as template

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.incident = ins()
        self.template = template()
        self.query_generator = query()
        self.logger = setup_logger(__name__)
        try:
            config = get_value_from_json_env_var('INTEGRATIONS_CONFIG', 'mindsdb_cloud')
            self.connection = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            cloud_temp = self.template.get_cloud_sql_api_template()
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)
                self.logger.error(f"Access denied for user: {config['user']}")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.logger.error(f"Database does not exist: {config['database']}")
            else:
                self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)
                self.logger.error(f"Connection could not be established: {err}")

    def tearDown(self):
        if self.connection.is_connected():
            self.connection.close()

    def test_connection_established(self):
        """
        Test that the connection to the MindsDB SQL API is established.
        """
        if not self.connection.is_connected():
            cloud_temp = self.template.get_cloud_sql_api_template()
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)
            raise Exception("Connection has not been established")

