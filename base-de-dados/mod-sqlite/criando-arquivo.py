import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_FOLDER = ROOT_DIR / 'db'
DB_NAME = 'db.sqlite3'
DB_FILE = DB_FOLDER / DB_NAME

Path.mkdir(DB_FOLDER, exist_ok=True)

TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

cursor.close()
connection.close()
