import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import db_config

# Connect to PostgreSQL
conn = db_config.connect_db()
cursor = conn.cursor()

# Fetch data from database
query = "SELECT title, views, likes, comments FROM videos;"
df = pd.read_sql(query, conn)

# Close the connection
cursor.close()
conn.close()

# Convert columns to numeric (PostgreSQL returns as strings)
df["views"] = pd.to_numeric(df["views"])
df["likes"] = pd.to_numeric(df["likes"])
df["comments"] = pd.to_numeric(df["comments"])


# 🔹 Bar Chart: Top 5 Most Viewed Videos
df_sorted = df.sort_values(by="views", ascending=False).head(5)
plt.figure(figsize=(10, 5))
plt.barh(df_sorted["title"], df_sorted["views"], color="skyblue")
plt.xlabel("Views")
plt.ylabel("Video Title")
plt.title("Top 5 Most Viewed Videos")
plt.gca().invert_yaxis()  # Invert Y-axis for better readability
plt.show()

# 🔹 Scatter Plot: Views vs. Likes
plt.figure(figsize=(8, 5))
plt.scatter(df["views"], df["likes"], color="red", alpha=0.5)
plt.xlabel("Views")
plt.ylabel("Likes")
plt.title("Views vs. Likes")
plt.show()