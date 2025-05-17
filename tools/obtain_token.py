import requests

def obtain_token(region, tenant_id, client_id, client_secret):
    """
    Obtain an access token from the Ruckus Cloud API.

    :param tenant_id: The ID of the tenant.
    :param client_id: The client ID for authentication.
    :param client_secret: The client secret for authentication.
    :return: The response from the API, which should contain the access token if successful.
    """
    url = f'https://{region}.ruckus.cloud/oauth2/token/{tenant_id}'
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    tenant_id = "1a504b89c85f4dbc8a485e7498240510"
    client_id = "cb86c32cd34d87f77b2b049f3434bd5d"
    client_secret = "a115e40a6fbf70d1236e3b601b1d46ae"
    region = "dev"
    token_response = obtain_token(region, tenant_id, client_id, client_secret)
    if token_response is not None:
        print(token_response)
