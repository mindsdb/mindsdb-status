import requests
import json
from datetime import datetime
import os


class InstatusClient:
    """
    A client for connecting to the Instatus API and reporting incidents.
    """

    def __init__(self):
        """
        Initialize the InstatusClient with the API key and base URL retrieved from environment variables.
        """
        self.api_key = os.environ.get('API_KEY')
        self.api_base_url = os.environ.get('API_BASE_URL')
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def connect(self):
        """
        Connect to the Instatus API and retrieve a list of status pages.

        Returns:
            list: A list of status pages in JSON format.
        """
        response = requests.get(
            f"{self.api_base_url}v2/status_pages",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def report_incident(self, page_id, name, message, components, status):
        """
        Report an incident to a specific status page using the Instatus API.

        Args:
            page_id (str): The ID of the status page to report the incident to.
            name (str): The name of the incident.
            message (str): A message describing the incident.
            components (str): The ID of the affected component.
            status (str): The status of the incident (e.g. "investigating").

        Returns:
            dict: The reported incident in JSON format.
        """
        payload = {
            "name": name,
            "message": message,
            "components": [components],
            "status": status,
            "started": datetime.now(),
            "notify": True,
            "statuses": [
                {
                    "id": components,
                    "status": "DEGRADEDPERFORMANCE"
                }
            ]
        }
        response = requests.post(
            f"{self.api_base_url}v1/{page_id}/incidents",
            json=json.dumps(payload, default=str),
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()
