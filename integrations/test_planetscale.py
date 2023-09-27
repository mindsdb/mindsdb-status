import unittest
from integrations.base_test import BaseTest
from utils.config import get_value_from_json_env_var, generate_random_db_name


class TestPlanetScaleConnection(BaseTest):
    """
    Test class for testing the PlanetScale datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new PlanetScale Datasource.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("planetscale_datasource")
            planetscale_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'planetscale')
            query = self.query_generator.create_database_query(
                random_db_name,
                "planet_scale",
                planetscale_config
            )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("PlanetScale", "clmqcnjoh110175brod4y64g93f")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()