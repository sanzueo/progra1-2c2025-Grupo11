import random
from nombres_teatroV2 import *
from datetime import datetime, timedelta

# Función para generar IDs de shows
def id_alt():
    n=random.randint(1000, 9999)
    while n in ids_shows:
        n=random.randint(1000, 9999)
    ids_shows.append(n)
    return n

# Función para generar fechas aleatorias de shows
def fecha_alt():
    fecha_inicio = datetime(2025, 1, 1)
    fecha_fin = datetime(2025, 12, 31)
    rango_dias = (fecha_fin - fecha_inicio).days
    dias_random = random.randint(0, rango_dias)
    fecha_aleatoria = fecha_inicio + timedelta(days=dias_random)
    return fecha_aleatoria.date()

# Crear 10 shows aleatorios
while len(datos_globales) != 10:
    id_show = id_alt()
    tipo_Evento = random.choice(tipos_show)
    duracion = random.choice([60,120,180])
    espectadores=0
    espacios_disponibles = 999
    fecha = fecha_alt()
    datos_globales.append([id_show, tipo_Evento, duracion, espectadores, espacios_disponibles, fecha])


#CREAR PRECIOS 

for i in datos_globales:
        id_show = i[0]
        precio_b = random.randint(7200,12000)
        precio_b2 = precio_b * 2
        precio_b3 = precio_b * 3

        precios_show.append([id_show,precio_b,precio_b2,precio_b3])

# Guardar solo los IDs de los shows
for i in datos_globales:
    solo_ids_show.append(i[0])

# Función para mostrar matriz de shows
def ver_m(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    columnas_t = ["ID's", "Tipo de evento", "Duración", "Cant. Espectadores", "Esp. Disponibles", "Fecha"]

    print("-" * 95)
    print(f"{'IDs':<8}  {'Tipo de evento':<18}  {'Duración':>10}  {'Cant. Espect.':>16}  {'Esp. Disp.':>14}  {'Fecha':>12}")
    print("-" * 95)

    for f in range(filas):
        print(f"{matriz[f][0]:<8}  {matriz[f][1]:<18}  {matriz[f][2]:>10}  {matriz[f][3]:>12}  {matriz[f][4]:>14} {str(matriz[f][5]):>18}")