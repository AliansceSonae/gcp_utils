import urllib3
import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

urllib3.disable_warnings()


def get_api(url: str, params: dict = None, **kwargs):
    """Sends a GET request.
        Args:
        - url (str): URL for the new :class:`Request` object.
        - params (dict): (optional) Dictionary, list of tuples or bytes to send
        - **kwargs: Optional arguments that ``request`` takes.
        Returns:
        - (tuple(`Response <Response>` object, int)): Response of request and the status code
    """
    try:
        s = requests.Session()
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
        s.mount('http://', HTTPAdapter(max_retries=retries))
        response = s.get(url, params=params, **kwargs, verify=False, timeout=560)
        response.raise_for_status()
    except requests.exceptions.HTTPError as httpErr:
        print("Http Error:", httpErr)
        return None, 501

    return response, response.status_code
