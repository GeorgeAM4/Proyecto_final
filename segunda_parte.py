# SEGUNDA PARTE DEL TRABAJO FINAL:)
 # AQUI ESTA EL BLOQUEO DE SEGURIDAD
clave = ""
while clave != "4502JORGE":  # AQUI ESTA LA CONTRASEÑA 
    clave = input("INGRESE LA CONTRASEÑA: ").strip()

print( "==================================")
print("=SISTEMA DE GESTION DE ESTUDIANTES=")
print("===================================")
print("ELIGE TU ROL:")
print("1. PROFESOR")
print("2. ESTUDIANTE")
print("3. SALIR")
opcion = ""
while opcion !="1" and opcion != "2":
    opcion = input("ELIGE TU ROL(1 o 2):").strip()
if  opcion == "1":
    print(" ELEGISTE PROFESOR, AQUI SE GESTIONA A LOS ESTUDIANTES.")
    #AQUI FALTA COMPLETAR LAS OPCIONES PARA EL PROFESOR 
if opcion == "1":
    print("MENU PROFESOR")
    print("1. AGREGAR NUEVO ESTUDIANTE")
    print("2. VER NOTAS DE LOS ESTUDIANTES")
    print("3. REGISTRAR ASISTENCIA")
    opcion_profesor = input("ELIGE UNA OPCION:").strip()

    if opcion_profesor == "1":
        nombre = input("INGRESA EL NOMBRE EL NUEVO ESTUDIANTE:")
        print(f"Estudiante { nombre } Agredao.")
    elif opcion_profesor == "2" : 
        print("AQUI PODRAS VER LAS NOTAS DE LOS ESTUDIANTES.")
    elif opcion_profesor == "3" :
        print("AQUI PODRAS REGISTRAR LA ASISTENCIA DE LOS ESTUDIANTES")   
    else:
        print("OPCION INVALIDA.")
elif opcion == "2" :
    print("MENU ESTUDIANTE")
    print("1. NOTAS ")
    print("2. ASISTENCIA ")
    print("3. TAREAS")
    opcion_estudiante = input("ELIGE UNA OPCION:").strip()

    if opcion_estudiante == "1":
        print(" CALIFICACIONES ")
    elif opcion_estudiante == "2" :
        print("ASISTENCIA")
    elif opcion_estudiante == "3" :
        print("TAREAS")
    else:
        print("OPCION INVALIDA.")
elif opcion =="3":
    print("SALIENDO DE LA PAGINA")

else:
    print("ERROR, ACTUALIZA LA PAGINA.")




