print("==================================")
print(" SISTEMA DE GESTION DE ESTUDIANTES")
print("==================================")
print("SELECCIONE UNA OPCION")
print("1. PROFESOR")
print("2. ESTUDIANTE")
opcion = input("ingrese una opcion:"). sprit()
#LA PARTE DEL PROFESOR
if opcion == "1":
usuario_correcto = "profesor"
contraseña = "040502002"
acceso = False 
while acceso == False:
    usuario = input("usuario:" ). sprit()
    password = input(" contraseña"). sprit()
if usuario == usuario_correcto and password == contraseña
print("ACCESO PERMITIDO")
print("BIENVENIDO AL SISTEMA DE PROFESORES")
acceso = True
else print("DATOS INCORRECTOS")
print("ACCESO DENEGADO")
# LA PARTE DEL ESTUDIANTE
elif opcion == "2":
usuario_correcto = "estuiante"
contraseña = 4502
acceso = False
while == False:
    usuario = input("usuario estudiante:"). sprit()
    contraseña = input("contraseña:"). sprit()
    if usuario == usuario_correcto and password == contraseña:
        print("BIENVENIDO QUERIDO ESTUDIANTE")
        acceso True
    else:
        print("DATS INCORRECTOS")
        print(" intentelo de nuevo")
    

