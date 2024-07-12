import sqlite3

"""
dbname = sightings.db
table: sightings
col 0: id
col 1: description
col 2: latitude
col 3: longitude
"""

class DatabaseHandler:
    """
    This class handles interactions with a SQLite database.

    Methods:
    - __init__(self, db_name): Initializes the DatabaseHandler object by connecting to the specified database.
    - create_table(self, table_name, columns): Creates a new table in the database with the given name and columns.
    - insert_into_table(self, table_name, values): Inserts a new row of values into the specified table.
    - fetch_from_table(self, table_name, columns='*', where=''): Fetches records from the specified table and returns the result.
    - delete_from_table(self, table_name, where=''): Deletes records from the specified table based on the given conditions.
    - update_table(self, table_name, set_data, where=''): Updates records in the specified table based on the given conditions.
    - find_coordinates(self, lat, lng): search db for row with matching latitude longitude and return entire row data as list
    - __del__(self): Closes the database connection when the object is destroyed.

    Example usage:
    db = DatabaseHandler('example.db')
    db.create_table('students', 'id INTEGER PRIMARY KEY, name TEXT, age INTEGER')
    db.insert_into_table('students', (1, 'John Doe', 18))
    db.fetch_from_table('students')
    db.delete_from_table('students', 'age < 18')
    db.update_table('students', 'age=20', 'name="John Doe"')
    db.find_coordinates(12.0123, -190.109123)
    """
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        cmd = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(cmd)

    def get_table_columns(self, table_name):
        self.cursor.execute(f"PRAGMA table_info({table_name})")
        return [column[1] for column in self.cursor.fetchall()]

    def insert_into_table(self, table_name, values):
        query = f"INSERT INTO {table_name} VALUES ({', '.join(['?' for _ in range(len(values))])})"
        self.cursor.execute(query, values)
        self.conn.commit()

    def fetch_from_table(self, table_name, columns='*', where=''):
        if where != '':
            where = 'WHERE ' + where
        cmd = f"SELECT {columns} FROM {table_name} {where}"
        self.cursor.execute(cmd)
        return self.cursor.fetchall()

    def delete_from_table(self, table_name, where=''):
        if where != '':
            where = 'WHERE ' + where
        cmd = f"DELETE FROM {table_name} {where}"
        self.cursor.execute(cmd)
        self.conn.commit()

    def update_table(self, table_name, set_data, where=''):
        if where != '':
            where = 'WHERE ' + where
        cmd = f"UPDATE {table_name} SET {set_data} {where}"
        self.cursor.execute(cmd)
        self.conn.commit()

    def find_coordinates(self, lat: float, lng: float) -> list:
        return self.fetch_from_table(table_name='sightings', columns='*', where=f'latitude = {lat} AND longitude = {lng}')

    def __del__(self):
        self.conn.close()


