import conexion

# Crear una instancia del conector de base de datos
# Ingresar la contraseña de su Local
conexion_bd = conexion.Conexion(
    host="localhost",
    user="root",
    password="",
    database="proyectointegradorv01"
)


def mostrar_dispositivos():
    conexion_bd.connect()
    listado = conexion_bd.leer_dispositivos()
    print("-" * 120)
    print("|{:^5s}|{:^15s}|{:^14s}|{:^20s}|{:^19s}|{:^19s}|{:^12s}".format(
        "ID", "MODELO", "NRO SERIE", "DIRECCION", "FECHA", "COORDENADAS", "ESTADO"))
    print("-" * 120)

    for dispositivo in listado:
        id_producto = str(dispositivo[0])
        modelo = dispositivo[1]
        nro_serie = dispositivo[2]
        direccion = dispositivo[3]
        fecha = dispositivo[4].strftime("%Y-%m-%d")
        coordenadas = str(dispositivo[5])
        estado = dispositivo[6]

        print("|{:^5s}|{:^15s}|{:^14s}|{:^20s}|{:^19s}|{:^19s}|{:^14s}".format(
            id_producto, modelo, nro_serie, direccion, fecha, coordenadas, estado))
        print("-"*120)


def insertar_dispositivo():
    conexion_bd.connect()
    modelo = input("Ingrese el modelo: ")
    nro_serie = input("Ingrese el numero de serie: ")
    direccion = input("Ingrese una direccion: ")
    fecha = input("Ingrese una fecha con este modelo (YY-MM-DD): ")
    coordenadas = input("Ingrese unas coordenadas: ")
    estado = input("Ingrese un estado: ")
    conexion_bd.ingresar_dispositivo(modelo, nro_serie, direccion, fecha, coordenadas, estado)


def actualizar_dispositivo():
    conexion_bd.connect()
    id_dispositivo = int(input("Ingrese el id del dispositivo que desea actualizar: "))
    modelo = input("Ingrese el modelo: ")
    nro_serie = input("Ingrese el numero de serie: ")
    direccion = input("Ingrese una direccion: ")
    fecha = input("Ingrese una fecha con este modelo (YY-MM-DD): ")
    coordenadas = input("Ingrese unas coordenadas: ")
    estado = input("Ingrese un estado: ")
    conexion_bd.modificar_dispositivo(modelo, nro_serie, direccion, fecha, coordenadas, estado, id_dispositivo)


def bajar_dispositivo():
    conexion_bd.connect()
    id_dispositivo = int(input("Ingrese el id del dispositivo que desea dar de baja: "))
    conexion_bd.eliminar_dispositivo(id_dispositivo)
