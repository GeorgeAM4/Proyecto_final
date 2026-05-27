# VARIABLES
clave_admin = "4502JORGE"
usuario_creado = ""
clave_usuario = ""

# PANTALLA DE BIENVENIDA
print("Hola, bienvenido al sistema de gestión de estudiantes.")
print("Por favor, seleccione una opción:")
print("1. Iniciar sesión")
print("2. Crear una cuenta")
print("3. Salir del sistema")

opcion_inicio = input("Ingrese una opción (1, 2, 3): ").strip()

# INICIAR SESIÓN
if opcion_inicio == "1":

    nombre_usuario = input("Ingrese su nombre: ").strip()
    contraseña = input("Ingrese su contraseña: ").strip()

    # ADMINISTRADOR
    if contraseña.upper() == clave_admin:

        print("==================================")
        print("= SISTEMA DE GESTIÓN DE ESTUDIANTES =")
        print("==================================")

        while True:

            print("ELIGE TU ROL:")
            print("1. PROFESOR")
            print("2. ESTUDIANTE")
            print("3. SALIR")

            opcion = input("Ingrese una opción (1, 2 o 3): ").strip()

            if opcion == "1":

                print("MENÚ PROFESOR")
                print("1. AGREGAR NUEVO ESTUDIANTE")
                print("2. VER NOTAS DE LOS ESTUDIANTES")
                print("3. REGISTRAR ASISTENCIA")
                print("4. SUMAR PUNTOS AL PROMEDIO")

                opcion_profesor = input("ELIGE UNA OPCIÓN: ").strip()

                if opcion_profesor == "1":

                    nombre = input("INGRESA EL NOMBRE DEL NUEVO ESTUDIANTE: ").strip().upper()

                    print(f"Estudiante {nombre} agregado.")

                elif opcion_profesor == "2":

                    print("AQUÍ PODRÁS VER LAS NOTAS DE LOS ESTUDIANTES.")

                elif opcion_profesor == "3":

                    print("AQUÍ PODRÁS REGISTRAR LA ASISTENCIA DE LOS ESTUDIANTES.")

                elif opcion_profesor == "4":

                    promedio = float(input("INGRESE EL PROMEDIO ACTUAL: "))
                    puntos = float(input("INGRESE LOS PUNTOS A SUMAR: "))

                    promedio += puntos

                    print(f"NUEVO PROMEDIO: {promedio}")

                else:

                    print("OPCIÓN INVÁLIDA.")

            elif opcion == "2":

                print("MENÚ ESTUDIANTE")
                print("1. NOTAS")
                print("2. ASISTENCIA")
                print("3. TAREAS")

                opcion_estudiante = input("ELIGE UNA OPCIÓN: ").strip()

                if opcion_estudiante == "1":

                    print("CALIFICACIONES")

                elif opcion_estudiante == "2":

                    print("ASISTENCIA")

                elif opcion_estudiante == "3":

                    print("TAREAS")

                else:

                    print("OPCIÓN INVÁLIDA.")

            elif opcion == "3":

                print("SALIENDO DEL SISTEMA. ¡GRACIAS POR VISITARNOS!")
                break

            else:

                print("OPCIÓN INVÁLIDA.")

    # USUARIO CREADO
    elif nombre_usuario == usuario_creado and contraseña == clave_usuario:

        print(f"Bienvenido {nombre_usuario}")

    else:

        print("USUARIO O CONTRASEÑA INCORRECTOS.")

# CREAR CUENTA
elif opcion_inicio == "2":

    usuario_creado = input("Ingrese un nombre de usuario: ").strip()
    clave_usuario = input("Ingrese una nueva contraseña: ").strip()

    print("CUENTA CREADA CORRECTAMENTE.")

# SALIR
elif opcion_inicio == "3":

    print("SALIENDO DEL SISTEMA. ¡GRACIAS POR VISITARNOS!")

# OPCIÓN INVÁLIDA
else:

    print("OPCIÓN INVÁLIDA.")
