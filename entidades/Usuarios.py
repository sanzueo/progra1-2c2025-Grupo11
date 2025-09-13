import random
from nombres_teatroV2 import id_usuarios,dni_usuarios,datos_globales_usuarios,nombres,ids_usuario


# Función para generar IDs de usuarios
def id_user():
    n=random.randint(1000,9999)
    while n in id_usuarios:
        n=random.randint(1000,9999)       
    id_usuarios.append(n)
    return n

def dni_user():
    dni = random.randint(16000000, 90000000)
    while dni in dni_usuarios:
        dni = random.randint(16000000, 90000000)
    dni_usuarios.append(dni)
    return dni
# Crear usuarios aleatorios a partir de nombres
while len(datos_globales_usuarios) != 5:
    id_usuario = id_user()
    nombre = random.choice(nombres).ljust(10, " ")
    dni=dni_user()
    telefono = random.randint(1100000000, 1199999999)
    correo = (nombre + random.choice(["@gmail.com","@hotmail.com","@yahoo.com"])).replace(" ", "")
    while len(correo) < 25:
        correo += " "
    estado = random.choice([True, False])

    datos_globales_usuarios.append([id_usuario, nombre, dni, telefono, correo, estado])

matriz3 = datos_globales_usuarios

# Guardar solo IDs y DNIs de usuarios activos
for i in datos_globales_usuarios:
    if i[5] == True:
        ids_usuario.append(i[0])

for i in datos_globales_usuarios:
    dni_usuarios.append(i[2])

# Función para mostrar matriz de usuarios
def ver_m3(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])

    columnas_t = ["ID","Nombre     ","DNI    ","        Telefono","Mail","                                Estado"]

    print("-"*111)
    for col in columnas_t:
        print(col, end="\t")
    print()
    print("-"*111)

    for f in range(filas):
        for c in range(columnas):
            #cada indice esta aclarado a la derecha
            if c == 0:  # ID
                print(str(matriz[f][c]).rjust(6), end="\t")
            elif c == 1:  # Nombre
                print(str(matriz[f][c]).ljust(12), end="\t")
            elif c == 2:  # DNI
                print(str(matriz[f][c]).rjust(10), end="\t")
            elif c == 3:  # Teléfono
                print(str(matriz[f][c]).rjust(12), end="\t")
            elif c == 4:  # Email
                print(str(matriz[f][c]).ljust(25), end="\t")
            elif c == 5:  # Estado
                estado_str = "ACTIVO" if matriz[f][c] == True else "INACTIVO"
                print(estado_str, end="\t")
        print()


