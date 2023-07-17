import psycopg2
from pytests.support.log_service import LogService

LOG = LogService


class PostgreUtils:

    @staticmethod
    def connection_postgre(params):
        try:
            connection = psycopg2.connect(
                host=params['host'],
                port=params['port'],
                database=params['database'],
                user=params['user'],
                password=params['password']
            )
        except Exception as e:
            LOG.log_error(f"Erro ao conectar no Banco: {e}")
        return connection

    @staticmethod
    def query_postgre(connection, query):
        results = []
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            col_names = [desc[0] for desc in cursor.description]
            for row in cursor.fetchall():
                result = {}
                for i, col_name in enumerate(col_names):
                    result[col_name] = row[i]
                results.append(result)
            cursor.close()
            connection.close()
            LOG.log_info(f"Query realizada: {results}")
        except Exception as e:
            cursor.close()
            connection.close()
            LOG.log_error(f"Erro recebido ao realizar a query: {e}")
        return results
