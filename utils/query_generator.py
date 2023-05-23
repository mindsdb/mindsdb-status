class QueryGenerator:
    """
    A helper class to generate SQL queries for MindsDB Actions.
    """

    @staticmethod
    def create_database_query(database_name: str, engine: str, parameters: dict) -> str:
        """
        Generate a CREATE DATABASE query with the given parameters.

        :param database_name: The name of the database to create.
        :param engine: The database engine to use.
        :param parameters: A dictionary of parameters for the engine.
        :return: The generated SQL query as a string.
        """
        parameter_str = ",\n  ".join([f'"{key}": "{value}"' for key, value in parameters.items()])
        query = f"""CREATE DATABASE {database_name}
                    WITH ENGINE = '{engine}',
                    PARAMETERS = {{
                    {parameter_str}
                }};"""
        return query
