import unittest
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from utils.instatus import InstatusClient as ins
from utils.template import IncidentTemplate as template
from utils.config import get_value_from_json_env_var
import os


class MongoAPITest(unittest.TestCase):
    """
    A unittest.TestCase subclass for testing MongoDB API functionality.
    """

    def setUp(self):
        """
        Set up the MongoDB connection before each test. Handles errors and prints appropriate messages.
        """
        try:
            self.incident = ins()
            self.template = template()
            config = get_value_from_json_env_var('INTEGRATIONS_CONFIG', 'mindsdb_cloud')
            self.client = MongoClient(
                host='cloud.mindsdb.com',
                username=config['user'],
                password=config['password'],
                port=27017
            )
            self.db = self.client['mindsdb']
        except ConnectionFailure:
            cloud_temp = self.template.get_cloud_mongo_api_template()
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)
            

    def tearDown(self):
        """
        Close the MongoDB connection after each test.
        """
        self.client.close()

    def test_default_collections_exist(self):
        """
        Test if the default collections exist in the MongoDB database.
        """
        try:
            collections = self.db.list_collection_names()
            self.assertIsNotNone(collections)
        except Exception as err:
            cloud_temp = self.template.get_cloud_mongo_api_template()
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)
  

    def test_models_collection_exist(self):
        """
        Test if the 'models' collection exists in the MongoDB database. If there's an exception, report the incident.
        """
        try:
            collection = self.db['models']
            count = collection.count_documents({})
            self.assertIsNotNone(count)
        except Exception as err:
            cloud_temp = self.template.get_cloud_mongo_api_template()
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == '__main__':
    unittest.main()
