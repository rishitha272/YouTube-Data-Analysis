import requests
import config
import csv

# YouTube API Key
API_KEY = config.YOUTUBE_API_KEY

# Replace with your channel ID (Google for Developers used here as an example)
channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"

# API URL to fetch the latest 10 video IDs from the channel
url = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={channel_id}&part=id&order=date&type=video&maxResults=10"

# Send request to YouTube API
response = requests.get(url)
data = response.json()

# Extract video IDs
video_ids = []
if "items" in data:
    for item in data["items"]:
        video_id = item["id"]["videoId"]
        video_ids.append(video_id)

# Fetch video statistics
video_details = []
if video_ids:
    video_ids_str = ",".join(video_ids)
    stats_url = f"https://www.googleapis.com/youtube/v3/videos?key={API_KEY}&id={video_ids_str}&part=snippet,statistics"

    response = requests.get(stats_url)
    video_data = response.json()

    for item in video_data["items"]:
        title = item["snippet"]["title"]
        views = item["statistics"].get("viewCount", "N/A")
        likes = item["statistics"].get("likeCount", "N/A")
        comments = item["statistics"].get("commentCount", "N/A")

        video_details.append([title, views, likes, comments])

# Save data to a CSV file
csv_file = "youtube_video_data.csv"

with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Views", "Likes", "Comments"])
    writer.writerows(video_details)

print(f"✅ Data saved to {csv_file}")


def get_videos():
    return video_details  # Returns the fetched video data

