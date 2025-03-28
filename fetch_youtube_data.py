import requests
import config

# YouTube API Key
API_KEY = config.YOUTUBE_API_KEY

# Replace with the Channel ID you want to analyze
channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"  # Google for Developers Channel ID

# API URL to get channel details
url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={channel_id}&key={API_KEY}"

# Send GET request
response = requests.get(url)
data = response.json()

# Extract channel details
if "items" in data:
    channel_info = data["items"][0]
    channel_name = channel_info["snippet"]["title"]
    subscribers = channel_info["statistics"]["subscriberCount"]
    total_views = channel_info["statistics"]["viewCount"]
    total_videos = channel_info["statistics"]["videoCount"]

    print("📌 YouTube Channel Details:")
    print(f"🔹 Channel Name: {channel_name}")
    print(f"🔹 Subscribers: {subscribers}")
    print(f"🔹 Total Views: {total_views}")
    print(f"🔹 Total Videos: {total_videos}")

else:
    print("❌ Error: No channel data found")
