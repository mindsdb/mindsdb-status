import unittest
import mysql.connector
from mysql.connector import errorcode
from utils.instatus import InstatusClient as ins
from utils.template import IncidentTemplate as template
from utils.config import get_value_from_json_env_var
import os


class MySQLAPITest(unittest.TestCase):
    """
    A unittest.TestCase subclass for testing MySQL API functionality.
    """

    def setUp(self):
        """
        Set up the MySQL connection before each test. Handles errors and prints appropriate messages.
        """
        try:
            self.incident = ins()
            self.template = template()
            config = get_value_from_json_env_var('INTEGRATIONS_CONFIG', 'mindsdb_cloud')
            self.cnx = mysql.connector.connect(
                user=config['user'],
                password=config['password'],
                host=config['host'],
                database='mindsdb'
            )
        except mysql.connector.Error as err:
            cloud_temp = self.template.get_website_template()
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)

    def tearDown(self):
        """
        Close the MySQL connection after each test.
        """
        self.cnx.close()

    def test_default_tables_exist(self):
        """
        Test if the default tables exist in the MySQL database.
        """
        cursor = self.cnx.cursor()
        query = "SHOW TABLES"
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            self.assertIsNotNone(result)
            cursor.close()
        except Exception as err:
            #TODO: map components id per incident
            cloud_temp = self.template.get_cloud_template()
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)
  

    def test_models_table_exist(self):
        """
        Test if the 'models' table exists in the MySQL database. If there's an exception, report the incident.
        """
        cursor = self.cnx.cursor()
        query = "SELECT * FROM models"
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            self.assertIsNotNone(result)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_cloud_template()
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == '__main__':
    unittest.main()
