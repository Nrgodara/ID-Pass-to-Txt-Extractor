import os

api_id = 29251040
api_hash = os.environ.get("API_HASH", "a1de34e4ad21cc9fb34798473eaf7bab")
bot_token = os.environ.get("BOT_TOKEN", "7062176093:AAHM8aqhPNbxiVa_JMZ0msApxuQOX1IpG24")
auth_users = os.environ.get("AUTH_USERS", "6539854720,1280494242")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "1280494242")
owner_users = [int(num) for num in osowner_users.split(",")]
