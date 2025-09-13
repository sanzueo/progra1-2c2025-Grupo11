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

# Guardar solo los IDs de los shows
for i in datos_globales:
    solo_ids_show.append(i[0])

# Función para mostrar matriz de shows
def ver_m(matriz):
    columnas_t = ["ID's", "Tipo de evento", "Duración", "Cant. Espectadores", "Esp. Disponibles", "Fecha", "Precio"]
    anchos = [12, 20, 10, 8, 14, 14, 14]

    print("-" * 94)
    print("".join(columnas_t[i].ljust(anchos[i]) for i in range(len(columnas_t))))
    print("-" * 94)

    for fila in matriz:
        id_show = fila[0]
        # Sumar precios de reservas de este show
        total_precio = sum(reserva[4] for reserva in datos_globales_reserva if reserva[3] == id_show)
        fila_str = [str(valor).ljust(anchos[i]) for i, valor in enumerate(fila)]
        fila_str.append(str(total_precio).ljust(anchos[-1]))
        print("".join(fila_str))