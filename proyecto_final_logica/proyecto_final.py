# PRIMERA PARTE DEL PROYECTO FINAL
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
elif  opcion == "2":
    print("ELEGISTE ESTUDIANTE, AQUI PODRAS VER TUS NOTAS, TAREAS Y DEMAS")
    #AQUI FALTA COMPLETAR LAS OPCIONES DEL ALUMNO 
else:
    print("OPCION NO VALIDA, REINICI LA PAGINA.")
