import random
from iniciacion_listas import datos_globales_reserva,ubicacion, ids_usuario, ids_reserva, datos_globales, shows_con_capacidad,precios_show
from entidades.shows import solo_ids_show
import json

def leer_reservas():
    while True:
        try:
            with open("datos_reserva", "r", encoding="utf-8") as archivo:
                reservas = []
                for linea in archivo:
                    linea = linea.strip()  # elimina saltos de línea
                    if linea:  # evita líneas vacías
                        partes = linea.split(";")
                        reservas.append(partes)
                return reservas
            break
        except FileNotFoundError:
            print("No se encontró el archivo de reservas.")
            continue
        except PermissionError:
            print("No tenés permiso para leer el archivo.")
            continue


with open("datos/datos_reservas.txt", "r", encoding="utf-8") as f_reservas:
    reservas_data=[]
    for linea in f_reservas:
        reservas = linea.strip().split(";")
        reservas_data.append(linea)
    

with open("datos/datos_show.json", "r", encoding="utf-8") as arch_shows:
    shows_cambio = json.load(arch_shows)
for reservas_lista in reservas_data:
    print (reservas)
    print (type(reservas))
    for id_reserva, id_usuario, sector, id_show, precio in reservas:
        id_show = int(id_show)
        for show in shows_cambio:
            if show["id-show"] == id_show:
                show["espectadores"] += 1
                show["espacios-disponibles"] -= 1
                break


with open("datos/datos_show.json", "w", encoding="utf-8") as f_shows:
    json.dump(shows_cambio, f_shows, ensure_ascii=False, indent=4)

print("Shows actualizados correctamente.")


# Función para generar IDs de reserva en forma aleatoria
def id_alt_r():
    n=random.randint(1000,19999)
    while n in ids_reserva:
        n = random.randint(1000, 19999)
    ids_reserva.append(n)
    return n

# Crear reservas aleatorias con el id de la reserva, el del usuario, la ubicacion y el precio de la reserva


def comparar_id_reserva(id_intento):
    lectura=leer_reservas()
    for reserva in lectura:
        id_reserva,id_usuario,ubicacion_u,show,precio=reserva
        if reserva[1]==id_intento:
            print("encontrado")
            return reserva


