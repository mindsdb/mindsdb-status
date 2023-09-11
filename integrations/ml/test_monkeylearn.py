import unittest
from utils.query_generator import QueryGenerator as query
from utils.config import generate_random_db_name
from integrations.base_test import BaseTest
from utils.config import generate_random_db_name

class TestMonkeyLearnConnection(BaseTest):
    """
    Test class for testing the Monkey Learn ML Engine using the MindsDB SQL API.
    """

    def test_create_ml_engine(self):
        """
        Create new Monkey Learn ML Engine.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("monkeylearn")
            query = self.query_generator.create_ml_engine_query(
                        random_db_name,
                        "monkeylearn",
                        {}
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("MonkeyLearn", "cllqbygse20980bdocblmt257p")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)

if __name__ == "__main__":
    unittest.main()
