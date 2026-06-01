# ==========================
# SISTEMA DE GESTION DE ESTUDIANTES
# ==========================

clave_admin = "4502JORGE"

usuarios = {}
estudiantes = []
notas = {}
asistencias = {}

while True:

    print("\n====================================")
    print(" SISTEMA DE GESTION DE ESTUDIANTES")
    print("====================================")
    print("1. Iniciar sesión")
    print("2. Crear cuenta")
    print("3. Salir")

    opcion_inicio = input("Seleccione una opción: ")

    if opcion_inicio == "3":
        print("Gracias por usar el sistema.")
        break

    elif opcion_inicio == "2":

        usuario = input("Nuevo usuario: ").upper()

        if usuario in usuarios:
            print("Ese usuario ya existe.")
            continue

        contraseña = input("Nueva contraseña: ")

        usuarios[usuario] = contraseña

        print("Cuenta creada correctamente.")

    elif opcion_inicio == "1":

        usuario = input("Usuario: ").upper()
        contraseña = input("Contraseña: ")

        acceso_correcto = False

        if usuario == "JORGE" and contraseña == clave_admin:
            acceso_correcto = True

        elif usuario in usuarios and usuarios[usuario] == contraseña:
            acceso_correcto = True

        if not acceso_correcto:
            print("Usuario o contraseña incorrectos.")
            continue

        while True:

            print("\nELIGE TU ROL")
            print("1. Profesor")
            print("2. Estudiante")
            print("3. Salir")

            rol = input("Seleccione una opción: ")

            # PROFESOR
            if rol == "1":

                while True:

                    print("\n===== MENU PROFESOR =====")
                    print("1. Agregar estudiante")
                    print("2. Registrar notas")
                    print("3. Ver notas")
                    print("4. Registrar asistencia")
                    print("5. Ver asistencia")
                    print("6. Ver cantidad de estudiantes")
                    print("7. Sumar puntos a promedio")
                    print("8. Salir")

                    opcion = input("Seleccione una opción: ")

                    if opcion == "1":

                        nombre = input("Nombre del estudiante: ").upper()

                        if nombre not in estudiantes:
                            estudiantes.append(nombre)
                            notas[nombre] = 0
                            asistencias[nombre] = "Sin registrar"

                        print("Estudiante agregado.")

                    elif opcion == "2":

                        nombre = input("Nombre del estudiante: ").upper()

                        if nombre not in estudiantes:
                            print("Estudiante no encontrado.")
                            continue

                        n1 = float(input("Nota 1: "))
                        n2 = float(input("Nota 2: "))
                        n3 = float(input("Nota 3: "))

                        promedio = (n1 + n2 + n3) / 3

                        notas[nombre] = promedio

                        print("Promedio guardado:", promedio)

                    elif opcion == "3":

                        print("\n===== NOTAS =====")

                        for estudiante, nota in notas.items():
                            print(estudiante, "->", nota)

                    elif opcion == "4":

                        nombre = input("Nombre del estudiante: ").upper()

                        if nombre not in estudiantes:
                            print("Estudiante no encontrado.")
                            continue

                        estado = input("Presente o Ausente: ")

                        asistencias[nombre] = estado

                        print("Asistencia registrada.")

                    elif opcion == "5":

                        print("\n===== ASISTENCIA =====")

                        for estudiante, estado in asistencias.items():
                            print(estudiante, "->", estado)

                    elif opcion == "6":

                        print("Cantidad de estudiantes:", len(estudiantes))

                    elif opcion == "7":

                        nombre = input("Nombre del estudiante: ").upper()

                        if nombre not in notas:
                            print("Estudiante no encontrado.")
                            continue

                        puntos = float(input("Puntos a sumar: "))

                        notas[nombre] += puntos

                        print("Nuevo promedio:", notas[nombre])

                    elif opcion == "8":

                        break

                    else:

                        print("Opción inválida.")

            # ESTUDIANTE
            elif rol == "2":

                while True:

                    print("\n===== MENU ESTUDIANTE =====")
                    print("1. Ver mis notas")
                    print("2. Ver mi asistencia")
                    print("3. Ver promedio final")
                    print("4. Salir")

                    opcion = input("Seleccione una opción: ")

                    if opcion == "1":

                        if usuario in notas:
                            print("Nota:", notas[usuario])
                        else:
                            print("No hay notas registradas.")

                    elif opcion == "2":

                        if usuario in asistencias:
                            print("Asistencia:", asistencias[usuario])
                        else:
                            print("No hay asistencia registrada.")

                    elif opcion == "3":

                        if usuario in notas:
                            print("Promedio final:", notas[usuario])
                        else:
                            print("No hay promedio registrado.")

                    elif opcion == "4":

                        break

                    else:

                        print("Opción inválida.")

            elif rol == "3":

                break

            else:

                print("Opción inválida.")

    else:

        print("Opción inválida.")
