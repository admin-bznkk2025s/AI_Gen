import requests
from msal import ConfidentialClientApplication
import os

client_id = os.environ["CLIENT_ID"]
tenant_id = os.environ["TENANT_ID"]
client_secret = os.environ["CLIENT_SECRET"]
user_email = os.environ["USER_EMAIL"]

authority = f"https://login.microsoftonline.com/{tenant_id}"
scopes = ["https://graph.microsoft.com/.default"]

app = ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)
token = app.acquire_token_for_client(scopes=scopes)

headers = {
    "Authorization": f"Bearer {token['access_token']}",
    "Content-Type": "application/json"
}

meeting_data = {
    "subject": "AI Operate Sync",
    "startDateTime": "2025-08-20T09:00:00",
    "endDateTime": "2025-08-20T10:00:00",
    "attendees": [{"emailAddress": {"address": user_email}, "type": "required"}]
}

response = requests.post(
    f"https://graph.microsoft.com/v1.0/users/{user_email}/calendar/events",
    headers=headers,
    json=meeting_data
)

print("Meeting created:", response.status_code, response.json())
