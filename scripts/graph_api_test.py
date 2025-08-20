import os
import requests
from msal import ConfidentialClientApplication

# โหลดค่าจาก environment variables หรือ GitHub Secrets
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
tenant_id = os.getenv("TENANT_ID")

# สร้าง MSAL client
app = ConfidentialClientApplication(
    client_id=client_id,
    client_credential=client_secret,
    authority=f"https://login.microsoftonline.com/{tenant_id}"
)

# ขอ access token
token_response = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
access_token = token_response.get("access_token")

# ตั้งค่า headers
headers = {
    "Authorization": f"Bearer {access_token}"
}

# 🔁 เปลี่ยน userPrincipalName ให้ตรงกับของคุณ
user_email = "taratorn.w@gablempn.onmicrosoft.com"
url = f"https://graph.microsoft.com/v1.0/users/{user_email}"

# เรียก Graph API
response = requests.get(url, headers=headers)

# แสดงผลลัพธ์
print("✅ Graph API Response:")
print(response.json())
