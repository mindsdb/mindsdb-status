import unittest
from utils.query_generator import QueryGenerator as query
from integrations.base_test import BaseTest
from utils.config import  get_value_from_json_env_var, generate_random_db_name


class TestMongoDBConnection(BaseTest):
    """
    Test class for testing the MongoDB datasource using MindsDB SQL API
    """

    def test_execute_query(self):
        """
        Create new MongoDB Datasource
        """
        try:
            cursor = self.connection.cursor()
            mongo_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'mongodb')
            random_db_name = generate_random_db_name("mongo_datasource")
            query = self.query_generator.create_database_query(
                        random_db_name,
                        "mongodb",
                         mongo_config
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("MongoDB", "clg3roq7d59296b5oiaro82erg")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
