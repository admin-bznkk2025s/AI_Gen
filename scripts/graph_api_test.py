from msal import ConfidentialClientApplication
import requests

# Setup credentials
client_id = "AZURE_CLIENT_ID"
client_secret = "AZURE_CLIENT_SECRET"
tenant_id = "secrets.AZURE_TENANT_ID"

# Create MSAL app
app = ConfidentialClientApplication(
    client_id=client_id,
    client_credential=client_secret,
    authority=f"https://login.microsoftonline.com/{tenant_id}"
)

# Acquire token
token = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])

# Debug print for token response
print("Token response:")
print(token)

# Check if access_token exists
if "access_token" in token:
    access_token = token["access_token"]

    # Call Graph API (replace with actual user email or ID)
    user_id = "user@example.com"  # ต้องเปลี่ยนเป็น email หรือ userPrincipalName ที่ถูกต้อง
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(
        f"https://graph.microsoft.com/v1.0/users/{user_id}/calendar/events",
        headers=headers
    )

    print("Graph API response:")
    print(response.json())
else:
    print("Failed to acquire access token.")
    if "error" in token:
        print("Error:", token["error"])
    if "error_description" in token:
        print("Error description:", token["error_description"])
