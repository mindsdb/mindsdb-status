import unittest
from utils.config import generate_random_db_name
from integrations.base_test import BaseTest


class TestOpenAIConnection(BaseTest):
    """
    Test class for testing the OpenAI ML Engine using the MindsDB SQL API.
    """

    def test_create_ml_engine(self):
        """
        Create new OpenAI ML Engine.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("openai")
            query = self.query_generator.create_ml_engine_query(
                        random_db_name,
                        "openai",
                        {}
                    )
            cursor.execute(query)
            cursor.close()
        except Exception:
            cloud_temp = self.template.get_integration_template("OpenAI", "clkmp25o097007ayokrpewimmf")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)

    '''
    TODO: Solve OpenAI timeouts
    def test_create_model(self):
        """
        Create new model using OpenAI.
        """
        try:
            cursor = self.connection.cursor()
            random_model_name = generate_random_db_name("oepanai")
            query = self.query_generator.create_model(
                        random_model_name,
                        "answer",
                        {
                            "engine": "openai",
                            "prompt_template" : "ask a question to a model"
                        }
                    )
            cursor.execute(query, multi=False)
            cursor.close()
        except Exception as err:
            self.logger.exception(err)
            assert False, f"Error executing query: {err}"
    '''


if __name__ == "__main__":
    unittest.main()
