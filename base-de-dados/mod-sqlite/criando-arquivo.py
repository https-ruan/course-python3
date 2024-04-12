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

# CUIDADO: fazendo delete sem where
cursor.execute(f'DELETE FROM {TABLE_NAME}')
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')

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

# Registrar valores nas colunas da tabela
# CUIDADO: sql injection
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    # '("Ruan Araujo", 85), '
    # '("Helena", 4.3)'
    '(:name, :weight)'
)
# cursor.execute(sql, ['Ruan Araujo', '85'])
# cursor.executemany(sql, [('Ruan Araujo', '85'), ('Helena', 4.3)])
# cursor.execute(sql, {"name": 'Ruan Araujo', "weight": 85})
cursor.executemany(
    sql,
    [
        {"name": 'Ruan Araujo', "weight": 85},
        {"name": 'Helena', "weight": 4.3}
    ]
)

connection.commit()

cursor.close()
connection.close()
