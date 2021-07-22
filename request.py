
import requests
import urllib3

urllib3.disable_warnings()

def get(url: str, params: dict = None, **kwargs):
    """Sends a GET request.
        Args:
        - url (str): URL for the new :class:`Request` object.
        - params (dict): (optional) Dictionary, list of tuples or bytes to send
        - **kwargs: Optional arguments that ``request`` takes.
        Returns:
        - (tuple(`Response <Response>` object, int)): Response of request and the status code
    """
    try:
        response = requests.get(url, params=params, **kwargs, verify=False)
        response.raise_for_status()
    except requests.exceptions.HTTPError as httpErr:
        print("Http Error:", httpErr)
    except requests.exceptions.ConnectionError as connErr:
        print("Error Connecting:", connErr)
    except requests.exceptions.Timeout as timeOutErr:
        print("Timeout Error:", timeOutErr)
    except requests.exceptions.RequestException as reqErr:
        print("Something Else:", reqErr)

    return response, response.status_code