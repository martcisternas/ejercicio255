usuario1 = None
usuario2 = None
usuario3 = None
contraseña1 = None
contraseña2 = None
contraseña3 = None

while True:
    print("-----Menu-----")
    print("1. Iniciar sesion")
    print("2. Registrar usuarios")
    print("3. Salir")
    #while True:
    try:
        opcion = int(input("Ingrese una opcion: "))
        #break
    except ValueError:
        print("Error, debe ingresar un numero.")
        continue

    if opcion == 1:
        
        if usuario1 == None and usuario2 == None and usuario3 == None:
            print("Debe ingresar un  usuario antes de iniciar sesión")
            continue
        
        usuario = input("Ingrese usuario")
        contrseña = input("Ingrese contraseña")
        if (usuario == usuario1 and contrseña == contraseña1) or (usuario == usuario2 and contrseña == contraseña2) or (usuario == usuario3 and contrseña == contraseña3): 
            print("Inicio de sesion correcto!")

            while True:
                print("--Menu de usuario--")
                print("1. Realizar llamada")
                print("2. Enviar correo electronico")
                print("3. Salir")
            
                try:
                    op = int(input("Seleccione una opcion: "))
                except ValueError:
                    print("ERROR!, Debe ingresar un número!")
                    continue

                if op == 1:
                    celular = input("Ingrese el numero del celular (9 Digitos, que comience con 9): ")
                    if len(celular) == 9 and celular.startswith(9) and celular.isdigit():
                        print("Llamando al celular: ",celular)
                    else:
                        print("ERROR!, Numero no es correcto.")

                elif op == 2:
                    correo = input("Ingrese su correo: ")
                    valido = False
                    for caracter in correo:
                        if caracter == "@" :
                            valido = True
                    
                    if valido :
                        mensaje = input ("Ingrese mensaje del correo: ")
                        print(f"Correo enviado a {correo} con mensaje: {mensaje}")

                    else:
                        print("Error correo no valido!")
                        
                elif op == 3:
                    print("Saliendo..")
                    break

        

    elif opcion == 2:
        print("Registro usuario")
        nuevoUsuario = input("Ingrese nuevo usuario")
        nuevaContraseña = input("Ingrese nueva contraseña")

        if usuario1 == None:
            usuario1 = nuevoUsuario
            contraseña1 = nuevaContraseña
        elif usuario2 == None:
            usuario2 = nuevoUsuario
            contraseña2 = nuevaContraseña
        elif usuario3 == None:
            usuario3 = nuevoUsuario
            contraseña3 = nuevaContraseña
        else:
            print("Error al ingresar usuario, máximo 3")
            continue

    elif opcion == 3:
        print("Saliendo...")
        break
    else:
        print("Opcion no valida")

    