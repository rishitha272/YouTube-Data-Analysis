import schedule
import time
import os

def fetch_and_store():
    print("Fetching and storing YouTube data...")
    os.system("python fetch_videos.py")
    os.system("python store_videos.py")

# Schedule the job to run every 6 hours
schedule.every(6).hours.do(fetch_and_store)


print("Scheduler started. Press Ctrl+C to stop.")

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)