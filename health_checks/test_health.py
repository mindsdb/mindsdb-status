import unittest
import requests
from utils.instatus import InstatusClient as ins
from utils.template import IncidentTemplate as template


class HealthCheckTests(unittest.TestCase):
    """
    A unittest.TestCase subclass for testing the health of MindsDB Website and docs.
    """

    def setUp(self):
        """
        Set up the Instatus client to report incidents
        """
        self.incident = ins()
        self.template = template()

    def test_health_check_docs(self):
        """
        Test if the docs.mindsdb.com URL is responding with a status code of 200 (OK).
        """
        url = "https://docs.mindsdb.com/"
        response = requests.get(url)
        #self.assertEqual(response.status_code, 200, f"Health check failed for {url}")
        if response.status_code is not 200:
            docs_temp = self.template.get_docs_template()
            self.incident.report_incident("cl8nll9g0106225olofc95s0wcm", docs_temp)
        
    def test_health_check_website(self):
        """
        Test if the mindsdb.com URL is responding with a status code of 200 (OK).
        """
        url = "https://mindsdb.com/"
        response = requests.get(url)
        if response.status_code is not 200:
            web_temp = self.template.get_website_template()
            self.incident.report_incident("cl8nll9g0106225olofc95s0wcm", web_temp)

if __name__ == '__main__':
    unittest.main()
