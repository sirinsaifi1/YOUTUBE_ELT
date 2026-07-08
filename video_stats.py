import requests
import json

API_KEY = "AIzaSyC8kIhaFapYQ70mKeQ6QZhubHR7eA5eKMs"
CHANNEL_HANDLE = "MrBeast"
url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"


response = requests.get(url)

print(response)
data = response.json()

json_data = json.dumps(data, indent=4)

print(json_data)

