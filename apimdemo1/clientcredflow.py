import os
import requests

# Set or retrieve your environment variables
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
TENANT_ID = os.environ.get('TENANT_ID')
# Choose the scope you need. For example:
SCOPE = "https://management.azure.com/.default"

# Construct the token endpoint URL
token_url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

# Prepare payload for token request
payload = {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "scope": SCOPE,
}

# Request the access token
token_response = requests.post(token_url, data=payload)
token_response.raise_for_status()  # raises an error for non-2xx responses
token = token_response.json().get("access_token")

if not token:
    raise Exception("Failed to retrieve access token")

# Use the access token to request your APIM endpoint
apim_endpoint = "https://apimgateway.srinman.com/echo/resource?param1=sample"
headers = {"Authorization": f"Bearer {token}"}
api_response = requests.get(apim_endpoint, headers=headers)
api_response.raise_for_status()

print("Status Code:", api_response.status_code)
print("Response:", api_response.text)