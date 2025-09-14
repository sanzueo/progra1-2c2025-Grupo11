import random
from nombres_teatroV2 import datos_globales_reserva,ubicacion, ids_usuario, ids_reserva, datos_globales, shows_con_capacidad,precios_show
from entidades.shows import solo_ids_show

# Función para generar IDs de reserva
def id_alt_r():
    n=random.randint(1000,9999)
    while n in ids_reserva:
        n = random.randint(1000, 9999)
    ids_reserva.append(n)
    return n


def shows_seleccion():

    show=random.choice(solo_ids_show)
    for i in datos_globales:
        if i[4] >0:
            shows_con_capacidad.append(i[0])    
    if show in shows_con_capacidad:
        show_elegido=show
    elif show not in shows_con_capacidad:
        show_elegido=random.choice(shows_con_capacidad)
    for i in datos_globales:
        if i[0] == show_elegido:
            i[3] += 1
            i[4] -= 1
    return show_elegido
# Crear reservas aleatorias
while len(datos_globales_reserva) != 10:
    id_reserva = id_alt_r()
    id_usuario = random.choice(ids_usuario)

    ubicacion_u = random.choice(ubicacion)

    show=shows_seleccion()

    if ubicacion_u == "platea    ":
        for i in precios_show:
            if i[0] == show:
                precio = i[1]

    elif ubicacion_u == "campo    ":
        for i in precios_show:
            if i[0] == show:
                    precio = i[2]
    elif ubicacion_u == "vip      ":
        for i in precios_show:
            if i[0] == show:
                    precio = i[3]
    

    
    datos_globales_reserva.append([id_reserva, id_usuario, ubicacion_u, show,precio])

# Función para mostrar reservas
def ver_m2(matriz):

    filas=len(matriz)
    inicio_Cont=int(input(f"\033[35mdesde que reserva deseas empezar: \033[0m"))
    while inicio_Cont < 0 or inicio_Cont >= filas:
        print(f"\033[35mNúmero fuera de rango, solo hay {filas-1} reservas seleccione dentro de ese rango\033[0m")
        inicio_Cont=int(input(f"desde que reserva deseas empezar: "))
    
    vision=int(input("\033[35mcuantos registros desde el inicio desea ver: \033[0m"))
    while vision < 1 or vision > (filas - inicio_Cont):
        print(f"\033[91m Debe ser entre 1 y {filas - inicio_Cont}\033[0m")
        vision = int(input("\033[35mcuántos registros desde el inicio deseas ver: \033[0m"))

    fin= inicio_Cont+vision

    columnas = len(matriz[0])
    columnas_t = ["ID'S","ID Usuario","Ubicación","ID Show","Precio"]
    print("-"*73)
    print(f"{'IDs':<8}  {'ID Usuario':<13}  {'ubicacion':>8}  {'ID Show':>12}  {'precio':>14}")  
    print("-"*73)
    for f in range(inicio_Cont, fin):
        print(f"{matriz[f][0]:<8}  {matriz[f][1]:<13}  {matriz[f][2]:>10}  {matriz[f][3]:>10}  {matriz[f][4]:>14}")