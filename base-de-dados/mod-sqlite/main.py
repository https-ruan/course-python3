import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Create Read   Update Delete
# SQL  - INSERT SELECT UPDATE DELETE

# CUIDADO: fazendo delete sem where
cursor.execute(f'DELETE FROM {TABLE_NAME}')

# DELETE mais cuidadoso
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
        {"name": 'Helena', "weight": 4.3},
        {"name": 'João', "weight": 12},
        {"name": 'Maria', "weight": 24},
    ]
)
connection.commit()


if __name__ == '__main__':
    print(sql)

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        f'WHERE id = 3'
    )
    connection.commit()

    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        f'SET name="QUALQUER", weight=67.89 '
        f'WHERE id = 1'
    )
    connection.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    connection.close()
