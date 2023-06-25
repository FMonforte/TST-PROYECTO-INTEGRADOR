import conexion

# Crear una instancia del conector de base de datos
conexion_bd = conexion.Conexion(host="localhost", user="root", password="31646323", database="proyectointegradorv01")
# Ingresar la contraseña de su Local
conexion_bd = conexion.Conexion(
    host="localhost",
    user="root",
    password="",
    database="proyectointegradorv01"
)

# Conectar a la base de datos
conexion_bd.connect()

print ("Empresa de IOT")
print ("Ingrese una opción")
print ("1. Ingresar Dispositivos")
print ("2. Consultar Dispositivos")
print ("Presione letra Q para salir")

opcion = input ("Seleccione una opcion: ")

opcion == "1":
conexion_bd.ingresar_dispositivo(modelo="Example", numero_de_serie="NroEx", direccion="DirEx", fecha="1990-01-01", coordenadas="CorEx", estado="EsEx")

elif opcion == "2":
    dispositivos = conexion_bd.leer_dispositivos() 
    for dispositivo in dispositivos
    print(dispositivo)     

elif opcion =="Q" or opcion == "q":    
    conexion_bd.disconnect()
    quit()

else:
print("Opcion no valida")    

conexion_bd.disconnect()

