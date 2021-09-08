from google.cloud import bigquery
from datetime import datetime


class BqClient:
    def __init__(self):
        self.client = bigquery.Client()

    def _query(self, sql: str):
        if sql is not None and sql != "":
            query_job = self.client.query(sql)
            res = query_job.result()
            return res

    def fetch_all(self, project_name: str, dataset: str, table: str, fields: list = []):
        if any([project_name is not None, dataset is not None, table is not None, fields is not None]):
            SQL = f"""
            SELECT
                {','.join(fields) if fields is not [] else '*'}
            FROM
                {project_name}.{dataset}.{table}
            """
            res = self._query(SQL)
            data = {'keys': [],
                    'data': []}
            if res.total_rows > 0:
                for field in res.schema:
                    data['keys'].append(field.name)

                for row in res:
                    data['data'].append(row.values())
            return data

    def get_max_datetime_field(self, project_name: str, dataset: str, table: str, field: str, trunc: str) -> datetime:
        SQL = f"""
            SELECT
            DATETIME_TRUNC(MAX({field}), {trunc})
            FROM
                {project_name}.{dataset}.{table}
            """
        res = self._query(SQL)
        if res.total_rows == 1:
            for row in res:
                return row.values()[0]
        return None

    def get_column_names(self, table_ref: str):
        table = self.client.get_table(table_ref)
        return [field.name for field in table.schema[:-1]]
