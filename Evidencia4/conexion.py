import mysql.connector


class Conexion:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        if self.connection.is_connected():
            print("Conexión exitosa")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Desconexión")

    def leer_dispositivos(self):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "SELECT * FROM Dispositivos"
            cursor.execute(query)
            dispositivos = cursor.fetchall()
            cursor.close()
            return dispositivos
        else:
            print("No hay conexión a la base de datos")

    def ingresar_dispositivo(self, modelo, numero_de_serie, direccion, fecha, coordenadas, estado):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "INSERT INTO Dispositivos (modelo, numero_de_serie, direccion_de_instalacion, fecha, coordenadas, "\
                    "estado) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (modelo, numero_de_serie, direccion, fecha, coordenadas, estado)
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            print("Datos insertados correctamente")
        else:
            print("No hay conexión a la base de datos")
