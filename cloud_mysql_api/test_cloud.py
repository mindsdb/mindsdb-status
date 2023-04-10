import unittest
import mysql.connector
from mysql.connector import errorcode
from cloud_mysql_api.insta_status import InstatusClient as ins
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
            self.cnx = mysql.connector.connect(
                user=os.environ.get('CLOUD_USER'),
                password=os.environ.get('CLOUD_PASS'),
                host='cloud.mindsdb.com',
                database='mindsdb'
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

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
        cursor.execute(query)

        results = cursor.fetchall()
        self.assertIsNotNone(results)
        cursor.close()

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
            inc = ins()
            #TODO: map components id per incident
            inc.report_incident("cl8nll9f7106187olof1m17eg17",
                                "MindsDB Cloud incident",
                                "We're currently investigating an issue with the Website",
                                "cl8nll9fr106215olofubk3u09d", 
                                "INVESTIGATING")


if __name__ == '__main__':
    unittest.main()
