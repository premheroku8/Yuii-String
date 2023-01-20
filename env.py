import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "12861350").strip()
API_HASH = os.getenv("API_HASH", "e1429ae7374edc95c986d652df783bf7").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "5619588117:AAGQVPs6LY3VpToYsORw49NbrpFtYl62Md8").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://yxghfmci:QkCv1t2hzOzHZz9J-my1xx9En3QgUvwC@ruby.db.elephantsql.com/yxghfmci").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "https://t.me/zennihhh")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
