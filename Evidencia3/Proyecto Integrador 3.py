import mysql.connector

midb = mysql.connector.connect(
host="localhost",
user="root",
password="Telecomunicaciones2023",
database="proyectoIntegradorv01"
)
print(midb)