from msal import ConfidentialClientApplication
import requests

# Setup credentials
client_id = "AZURE_CLIENT_ID"
client_secret = "AZURE_CLIENT_SECRET"
tenant_id = "27f15384-cfc8-4f6c-b768-d0f59c1de5af"

# Get token
app = ConfidentialClientApplication(
    client_id=client_id,
    client_credential=client_secret,
    authority=f"https://login.microsoftonline.com/{tenant_id}"
)

token = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
access_token = token["access_token"]

# Call Graph API
headers = {"Authorization": f"Bearer {access_token}"}
response = requests.get(
    "https://graph.microsoft.com/v1.0/me/calendar/events",
    headers=headers
)

print(response.json())
