import sqlite3
from sqlite3 import Error

conn = None
try:
    conn = sqlite3.connect("database.sqlite")
except Error as e:
    print(e)
finally:
    if conn:
        conn.close()
env_vars = [
    "DISCORD_API_KEY",
    "IMGUR_API_KEY",
    "IMGUR_API_SECRET",
    "OPENAI_API_KEY",
    "TENOR_API_KEY",
    "ADMIN_USER_ID",
    "ADDITIONAL_SYNC_PERMISSIONS",
    "ERROR_LOG_CHANNEL_ID",
    "DEV_REPO_URL",
]
try:
    with open(".devcontainer/.env", "x") as file:
        content = [var + "=\n" for var in env_vars]
        file.writelines(content)

except FileExistsError:
    pass
