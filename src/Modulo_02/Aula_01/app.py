import MySQLdb
from connection_factory import ConnectionFactory

connection = ConnectionFactory().get_connection()

cursor = connection.cursor()

cursor.execute('SELECT * from cursos')

for linha in cursor:
    print(linha)

connection.close()