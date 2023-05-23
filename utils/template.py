from datetime import datetime

class IncidentTemplate():


    def get_website_template(self):
        incident = {
            "name": "MindsDB Website incident",
            "message": "We're currently investigating an issue with the MindsDB website",
            "components": ["cl8nll9g0106225olofc95s0wcm"],
            "status": "INVESTIGATING",
            "started": str(datetime.now()),
            "notify": True,
            "statuses": [
                {
                    "id": "cl8nll9g0106225olofc95s0wcm",
                    "status": "MAJOROUTAGE"
                }
            ]
        }
        return incident
    
    def get_docs_template(self):
        incident = {
            "name": "MindsDB Docs incident",
            "message": "We're currently investigating an issue with the Documentation website",
            "components": ["cl8nll9g9106235olof6ovwhb7u"],
            "status": "INVESTIGATING",
            "started": str(datetime.now()),
            "notify": True,
            "statuses": [
                {
                    "id": "cl8nll9g9106235olof6ovwhb7u",
                    "status": "MAJOROUTAGE"
                }
            ]
        }
        return incident
    
    def get_cloud_template(self):
        incident = {
            "name": "MindsDB Cloud incident",
            "message": "We're currently investigating an issue with MindsDB Cloud",
            "components": ["cl8nll9fr106215olofubk3u09d"],
            "status": "INVESTIGATING",
            "started": str(datetime.now()),
            "notify": True,
            "statuses": [
                {
                    "id": "cl8nll9fr106215olofubk3u09d",
                    "status": "MAJOROUTAGE"
                }
            ]
        }
        return incident
    
    def get_mysql_template(self):
        incident = {
            "name": "MindsDB MySQL Integration Incident",
            "message": "We're currently investigating an issue with the MySQL Integration",
            "components": ["clg3rmxx157961bdoi3zyenisn"],
            "status": "INVESTIGATING",
            "started": str(datetime.now()),
            "notify": True,
            "statuses": [
                {
                    "id": "clg3rmxx157961bdoi3zyenisn",
                    "status": "MAJOROUTAGE"
                }
            ]
        }
        return incident
