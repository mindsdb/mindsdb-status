import unittest
from utils.config import generate_random_db_name
from integrations.base_test import BaseTest


class TestLlamaIndexConnection(BaseTest):
    """
    Test class for testing the LlamaIndex ML Engine using the MindsDB SQL API.
    """

    def test_create_llamaIndex_engine(self):
        """
        Create new LlamaIndex ML Engine.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("llamaIndex_engine")
            query = self.query_generator.create_ml_engine_query(
                        random_db_name,
                        "llama_index",
                        {}
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("LlamaIndex", "clmj7gifd11472bloft7hepijv")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
