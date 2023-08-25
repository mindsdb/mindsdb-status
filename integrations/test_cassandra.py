import unittest
import mysql.connector
from mysql.connector import errorcode
from utils.query_generator import QueryGenerator as query
from utils.config import  get_value_from_json_env_var, generate_random_db_name
from utils.log import setup_logger
from utils.instatus import InstatusClient as ins
from utils.template import IncidentTemplate as template


class TestCassandraConnection(unittest.TestCase):
    """
    Test class for testing the Apache Cassandra datasource using the MindsDB SQL API.
    """

    def setUp(self):
        """
        Set up the test environment by establishing a connection to the MindsDB SQL API.
        """
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
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)

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
        if not self.connection.is_connected():
            cloud_temp = self.template.get_cloud_sql_api_template()
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)

    def test_execute_query(self):
        """
        Create a new Cassandra Datasource.
        """
        try:
            cursor = self.connection.cursor()
            cassandra_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'cassandra')
            random_db_name = generate_random_db_name("cassandra_datasource")
            query = self.query_generator.create_database_query(
                        random_db_name,
                        "cassandra",
                         cassandra_config
            )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Apache Cassandra", "cllqcoaqd36506bkocxx5fjnny")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
