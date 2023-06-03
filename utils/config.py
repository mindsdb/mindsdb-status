import os
import random

MYSQL_API_CONFIG = {
    'user': os.environ.get('MINDSDB_CLOUD_USER'),
    'password': os.environ.get('MINDSDB_CLOUD_PASS'),
    'host': 'cloud.mindsdb.com',
    'database':'mindsdb'
}

MYSQL_CONFIG = {
    "user": "mocked_user",
    "password": "mocked_password",
    "host": "mocked_host",
    "port": "mocked_port",
    "database": "mocked_database"
}

MARIADB_CONFIG = {
    "user": "mocked_user",
    "password": "mocked_password",
    "host": "mocked_host",
    "port": "mocked_port",
    "database": "mocked_database"
}

SINGLESTORE_CONFIG = {
    "user": "mocked_user",
    "password": "mocked_password",
    "host": "mocked_host",
    "port": "mocked_port",
    "database": "mocked_database"
}

CLICKHOUSE_CONFIG = {
    "user": "mocked_user",
    "password": "mocked_password",
    "host": "mocked_host",
    "port": "mocked_port",
    "database": "mocked_database"
}

SNOWFLAKE_CONFIG = {
    "host": "mocked_host",
    "user": "mocked_user",
    "password": "mocked_password",
    "account": "mocked_account",
    "warehouse": "mocked_warehouse",
    "schema": "mocked_schema",
    "database": "mocked_database",
    "protocol": "mocked_protocol",
    "port": "mocked_port"
}

DATABRICKS_CONFIG = {
    "server_hostname": "mocked_server_hostname",
    "http_path": "mocked_http_path",
    "access_token": "mocked_access_token",
    "schema": "mocked_schema"
}


def generate_random_db_name(base_name: str, min_value: int = 1000, max_value: int = 9999) -> str:
    """
    Generates a random database name by appending a random number to the base name.

    :param base_name: The base name for the database.
    :param min_value: The minimum value for the random number (inclusive).
    :param max_value: The maximum value for the random number (inclusive).
    :return: The generated database name as a string.
    """
    random_number = random.randint(min_value, max_value)
    return f"{base_name}_{random_number}"