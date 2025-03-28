import psycopg2
from db_config import connect_db

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS youtube_videos (
        video_id VARCHAR(50) PRIMARY KEY,
        title TEXT,
        description TEXT,
        published_at TIMESTAMP,
        view_count BIGINT,
        like_count BIGINT,
        comment_count BIGINT
    );
    """
    
    cursor.execute(create_table_query)
    conn.commit()
    
    cursor.close()
    conn.close()
    print("Table created successfully!")

create_table()
