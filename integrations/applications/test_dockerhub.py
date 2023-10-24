import unittest
from integrations.base_test import BaseTest
from utils.config import generate_random_db_name, get_value_from_json_env_var


class TestDockerHubConnection(BaseTest):
    """
    Test class for testing the Docker Hub datasource using the MindsDB SQL API.
    """

    def test_execute_query(self):
        """
        Create a new Docker Hub Datasource.
        """
        try:
            cursor = self.connection.cursor()
            random_db_name = generate_random_db_name("dockerhub_datasource")
            dockerhub_config = get_value_from_json_env_var("INTEGRATIONS_CONFIG", 'dockerhub')
            query = self.query_generator.create_database_query(
                        random_db_name,
                        "dockerhub",
                        dockerhub_config
                    )
            cursor.execute(query)
            cursor.close()
        except Exception as err:
            cloud_temp = self.template.get_integration_template("Docker Hub", "clnx9m44t2220biomtbyws863")
            self.incident.report_incident("cl8nll9f7106187olof1m17eg17", cloud_temp)


if __name__ == "__main__":
    unittest.main()
