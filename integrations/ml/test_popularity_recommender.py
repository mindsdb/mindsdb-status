import unittest

from integrations.base_test import BaseTest
from utils.config import generate_random_db_name

class TestPopularityRecommenderConnection(BaseTest):
    """
    Test class for testing the Popularity Recommender ML Engine using the MindsDB SQL API.
    """

    def test_create_popularity_recommender_engine(self):
        """
        Create new Popularity Recommender ML Engine.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("popularity_recommender_engine")
            query = self.query_generator.create_ml_engine_query(
                random_db_name,
                "popularity_recommender",
                {}
            )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Popularity Recommender", "cloik7rx01436bcoj26wervhl")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)

if __name__ == "__main__":
    unittest.main()
