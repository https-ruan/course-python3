import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_FOLDER = ROOT_DIR / 'db'
DB_NAME = 'db.sqlite3'
DB_FILE = DB_FOLDER / DB_NAME

Path.mkdir(DB_FOLDER, exist_ok=True)

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# SQL

cursor.close()
connection.close()
