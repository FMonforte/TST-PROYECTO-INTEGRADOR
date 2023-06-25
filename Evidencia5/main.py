import controlador

while True:
    print("Empresa de IOT")
    print("Ingrese una opción")
    print("1. Ingresar Dispositivos")
    print("2. Consultar Dispositivos")
    print("Presione letra Q para salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        controlador.insertar_dispositivo()

    elif opcion == "2":
        controlador.mostrar_dispositivos()

    elif opcion == "3":
        controlador.actualizar_dispositivo()

    elif opcion == "4":
        controlador.bajar_dispositivo()

    elif opcion == "Q" or opcion == "q":
        quit()

    else:
        print("Opcion no valida")
