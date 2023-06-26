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

    def modificar_dispositivo(self, modelo, numero_serie, direccion, fecha, coordenadas, estado, id_dispositivo):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "UPDATE Dispositivos SET modelo= %s, numero_de_serie= %s, direccion_de_instalacion= %s, " \
                    "fecha= %s, coordenadas= %s, estado= %s WHERE id_dispositivos= %s"
            values = (modelo, numero_serie, direccion, fecha, coordenadas, estado, id_dispositivo)
            cursor.execute(query, values)
            self.connection.commit()
            print("Datos incertados correctamente")
        else:
            print("No hay conexion a la base de datos")

    def eliminar_dispositivo(self, id_dispositivo):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "DELETE from Dispositivos WHERE id_dispositivos = %s"
            values = [id_dispositivo]
            cursor.execute(query, values)
            self.connection.commit()
            print("Registro eliminado correctamente")
        else:
            print("No hay conexion a la base de datos")