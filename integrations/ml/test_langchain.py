import unittest
from utils.config import generate_random_db_name
from integrations.base_test import BaseTest


class TestLangchainConnection(BaseTest):
    """
    Test class for testing the Langchain ML Engine using the MindsDB SQL API.
    """

    def test_create_Langchain_engine(self):
        """
        Create new Langchain ML Engine.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("langchain_engine")
            query = self.query_generator.create_ml_engine_query(
                        random_db_name,
                        "langchain",
                        {}
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Langchain", "clmj5oz86105583c7n5np5g6jx4")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
