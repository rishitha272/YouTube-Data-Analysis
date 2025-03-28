import psycopg2
import fetch_videos
import db_config  # Ensure this contains your PostgreSQL credentials

# PostgreSQL Connection Config
# DB_HOST = db_config.host
# DB_NAME = db_config.dbname
# DB_USER = db_config.user
# DB_PASSWORD = db_config.password

def store_video_data():
    try:
        # Connect to PostgreSQL
        conn = conn = db_config.connect_db()
        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            id SERIAL PRIMARY KEY,
            title TEXT,
            views BIGINT,
            likes BIGINT,
            comments BIGINT
        )
        ''')

        # Fetch video data
        videos = fetch_videos.get_videos()  # Ensure fetch_videos.py has a `get_videos()` function

        # Insert video data into PostgreSQL
        for video in videos:
            cursor.execute(
                "INSERT INTO videos (title, views, likes, comments) VALUES (%s, %s, %s, %s)",
                video
            )

        # Commit and close connection
        conn.commit()
        cursor.close()
        conn.close()

        print("✅ Data stored in PostgreSQL successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")

# Run the function
store_video_data()
