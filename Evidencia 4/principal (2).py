import conexion

# Crear una instancia del conector de base de datos
# Ingresar la contraseña de su Local
conexion_bd = conexion.Conexion(
    host="localhost",
    user="root",
    password="",
    database="proyectointegradorv01"
)

# Conectar a la base de datos
conexion_bd.connect()

# Leer los dispositivos desde la tabla
dispositivos = conexion_bd.leer_dispositivos()
for dispositivo in dispositivos:
    print(dispositivo)

print("Fin tabla dispositivos")


# Ingresar dispositivo en la tabla
conexion_bd.ingresar_dispositivo(
    modelo="Example", numero_de_serie="NroEx", direccion="DirEx", fecha="1990-01-01", coordenadas="CorEx", estado="EsEx")

dispositivos = conexion_bd.leer_dispositivos()
for dispositivo in dispositivos:
    print(dispositivo)

print("Fin tabla dispositivos")

# Desconectar de la base de datos
conexion_bd.disconnect()