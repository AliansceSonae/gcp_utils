import json
from google.cloud import storage


def mount_path(dataset: str, table: str, file_name: str, use_hive: bool = False, delimiter: str = "/", ** custom_params):
    base_path = f"{dataset}{delimiter}{table}{delimiter}"

    for key, value in custom_params.items():
        if use_hive:
            base_path += f"{key}={value}{delimiter}"
        else:
            base_path += f"{value}{delimiter}"

    return base_path + file_name


def upload_json_data(bucket_name: str, blob_name: str, data: dict):
    bucket = storage.Client().get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(json.dumps(data, ensure_ascii=False).encode("utf-8"), timeout=540, content_type="application/json")
    return blob_name

def upload_csv_data(bucket_name: str, blob_name: str, data: str):
    bucket = storage.Client().get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(data, timeout=540, content_type="text/csv")
    return blob_name
