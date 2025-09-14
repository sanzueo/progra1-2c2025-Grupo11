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
while len(datos_globales_usuarios) != 50:
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

    inicio_Cont=int(input(f"desde que reserva deseas empezar: "))
    while inicio_Cont < 0 or inicio_Cont >= filas:
        print(f"Número fuera de rango, solo hay {filas-1} reservas seleccione dentro de ese rango")
        inicio_Cont=int(input(f"desde que reserva deseas empezar: "))
    
    vision=int(input("cuantos registros desde el inicio desea ver"))
    while vision < 1 or vision > (filas - inicio_Cont):
        print(f"Debe ser entre 1 y {filas - inicio_Cont}")
        vision = int(input("cuántos registros desde el inicio deseas ver: "))

    columnas_t = ["ID","Nombre     ","DNI    ","        Telefono","Mail","                                Estado"]

    fin=inicio_Cont+vision
    print("-"*91)
    print(f"{'ID':<8}  {'nombre':<13}  {'DNI':>8}  {'Telefono':>14}  {'Mail':>14} {'Estado':>23}")  
    print("-"*91)
    for f in range(inicio_Cont, fin):
        if matriz[f][5] == True:
            estado = "ACTIVO"
        else:
            estado= "INACTIVO"
        print(f"{matriz[f][0]:<8}  {matriz[f][1]:<13}  {matriz[f][2]:>10}  {matriz[f][3]:>15}  {matriz[f][4]:>18} {estado:>10}")