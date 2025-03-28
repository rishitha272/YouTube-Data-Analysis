import psycopg2

# Database connection function
def connect_db():
    return psycopg2.connect(
        dbname="youtube_data",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )
