import os
from msal import ConfidentialClientApplication
import requests

# Load credentials from environment variables
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
tenant_id = os.getenv("TENANT_ID")

# ตรวจสอบว่าค่าถูกโหลดมาจริง
print("Loaded environment variables:")
print("CLIENT_ID:", client_id)
print("TENANT_ID:", tenant_id)

# Validate
if not all([client_id, client_secret, tenant_id]):
    raise ValueError("Missing one or more required environment variables: CLIENT_ID, CLIENT_SECRET, TENANT_ID")

# Create MSAL app
app = ConfidentialClientApplication(
    client_id=client_id,
    client_credential=client_secret,
    authority=f"https://login.microsoftonline.com/{tenant_id}"
)

# Acquire token
token = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])

# Debug print
print("Token response:")
print(token)

if "access_token" in token:
    access_token = token["access_token"]

    # Replace with actual user email or ID
    user_id = "bznkk2000_hotmail.com#EXT#@bznkk2000hotmail.onmicrosoft.com"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(
        f"https://graph.microsoft.com/v1.0/users/{user_id}/calendar/events",
        headers=headers
    )

    print("Graph API response:")
    print(response.json())
else:
    print("Failed to acquire access token.")
    print("Error:", token.get("error"))
    print("Error description:", token.get("error_description"))
