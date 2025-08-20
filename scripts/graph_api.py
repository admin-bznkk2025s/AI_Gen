
def get_recent_meetings(user_email):
    print(f"Fetching recent meetings for {user_email}...")
    return [
        {"subject": "Team Sync", "attendees": [user_email], "transcript": "Discussed project updates."}
    ]
