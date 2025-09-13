import random
from nombres_teatroV2 import datos_globales_reserva,ubicacion, ids_usuario, ids_reserva, datos_globales, shows_con_capacidad,precios_show
from entidades.shows import solo_ids_show

# Función para generar IDs de reserva
def id_alt_r():
    n=random.randint(1,1000)
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
while len(datos_globales_reserva) != 30:
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
    columnas_t = ["ID'S","ID Usuario","Ubicación","ID Show","Precio"]
    print("-"*50)
    print("\t".join(columnas_t))
    print("-"*50)
    for fila in matriz:
        print("\t".join(str(c) for c in fila))