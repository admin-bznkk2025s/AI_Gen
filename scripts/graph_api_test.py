import os
import requests
from msal import ConfidentialClientApplication

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
tenant_id = os.getenv("TENANT_ID")

app = ConfidentialClientApplication(
    client_id=client_id,
    client_credential=client_secret,
    authority=f"https://login.microsoftonline.com/{tenant_id}"
)

token = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
access_token = token["access_token"]

headers = {"Authorization": f"Bearer {access_token}"}
response = requests.get("https://graph.microsoft.com/v1.0/me", headers=headers)

print("✅ Graph API Response:")
print(response.json())
