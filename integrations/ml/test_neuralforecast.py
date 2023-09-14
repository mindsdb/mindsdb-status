import unittest
from utils.config import generate_random_db_name
from integrations.base_test import BaseTest


class TestNeuralForecastConnection(BaseTest):
    """
    Test class for testing the NeuralForecast ML Engine using the MindsDB SQL API.
    """

    def test_create_neuralforecast_engine(self):
        """
        Create new NeuralForecast ML Engine.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("neuralforecast_engine")
            query = self.query_generator.create_ml_engine_query(
                        random_db_name,
                        "Neuralforecast",
                        {}
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Nixtla's NeuralForecast", "clmj4968l67245c7n5f7ynr8y5")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
