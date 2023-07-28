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
    
    def get_cloud_sql_api_template(self):
        incident = {
            "name": "MindsDB Cloud SQL API Incident",
            "message": "We're currently investigating an issue with the SQL API",
            "components": ["clkmhsh0a4312bsoo8m81fcni"],
            "status": "INVESTIGATING",
            "started": str(datetime.now()),
            "notify": True,
            "statuses": [
                {
                    "id": "clkmhsh0a4312bsoo8m81fcni",
                    "status": "MAJOROUTAGE"
                }
            ]
        }
        return incident
    
    def get_cloud_mongo_api_template(self):
        incident = {
            "name": "MindsDB Cloud Mongo API Incident",
            "message": "We're currently investigating an issue with the Mongo API",
            "components": ["clkmia49615713bloogwmq41vp"],
            "status": "INVESTIGATING",
            "started": str(datetime.now()),
            "notify": True,
            "statuses": [
                {
                    "id": "clkmia49615713bloogwmq41vp",
                    "status": "MAJOROUTAGE"
                }
            ]
        }
        return incident
    def get_integration_template(self, integration_name, component_id):
        incident = {
            "name": f"MindsDB {integration_name} Incident",
            "message": "We're currently investigating an issue with the {integration_name} integration",
            "components": [component_id],
            "status": "INVESTIGATING",
            "started": str(datetime.now()),
            "notify": True,
            "statuses": [
                {
                    "id": component_id,
                    "status": "MAJOROUTAGE"
                }
            ]
        }
        return incident
