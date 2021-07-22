from google.cloud.secretmanager import SecretManagerServiceClient


def get(client: SecretManagerServiceClient, project_number: int, name: str, version: int = 1):
    """Function to get one secret

    Args:
        client (SecretManagerServiceClient): Client of Secret Manager
        project_number (int): Number of project to access the secrets
        name (str): Name of the secret
        version (int, optional): The version of secret. Defaults to 1.

    Returns:
        (str): Value of secret
    """
    if not client:
        client = SecretManagerServiceClient()

    if all([project_number is not None, name is not None, version is not None]):
        response = client.access_secret_version(
            {'name': f"projects/{project_number}/secrets/{name}/versions/{version}"})
        return response.payload.data.decode("UTF-8")
    return None


def load_secrets(secrets_names: list, project: int) -> dict:
    """Function to load many secrets passing a list of names and the project 

    Args:
        secrets_names (list): List of name of secrets
        project (int): Number of project to access the secrets

    Returns:
        (dict): Dict that contains the names of secrets in keys and value of secret
    """
    s_client = SecretManagerServiceClient()
    response = {}
    for name in secrets_names:
        response[name] = get(s_client, project_number=project, name=name)

    return response
