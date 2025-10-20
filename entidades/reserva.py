import random
from nombres_teatroV2 import datos_globales_reserva,ubicacion, ids_usuario, ids_reserva, datos_globales, shows_con_capacidad,precios_show
from entidades.shows import solo_ids_show

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


#funcion para buscar reservas mostrando las del usuario que hizo esas reservas
def ver_busqueda_reserva(matriz):

    filas=len(matriz)

    print(f"\033[32m{'-'*73}\033[0m")
    print(f"\033[32m{'IDs':<8}  {'ID Usuario':<13}\033  \033[35m{'Ubicación':>10}  {'ID Show':>12}\033[0m  \033[34m{'Precio':>14}\033[0m")
    print(f"\033[32m{'-'*73}\033[0m")
    for f in range(filas):
        print(f"\033[32m{matriz[f][0]:<8}  {matriz[f][1]:<13}\033[35m  {matriz[f][2]:>10}  {matriz[f][3]:>10}\033[0m  \033[34m{matriz[f][4]:>14}\033[0m")

# Función para mostrar reservas con sistema de filtrado por cantidad
def ver_m2(matriz):

    filas=len(matriz)
    inicio_Cont=int(input(f"\033[35mDesde que reserva deseas empezar: \033[0m"))
    while inicio_Cont < 0 or inicio_Cont >= filas:
        print(f"\033[91mNúmero fuera de rango, solo hay {filas-1} reservas. Seleccione dentro de ese rango\033[0m")
        inicio_Cont=int(input(f"Desde que reserva deseas empezar: "))
    
    vision=int(input("\033[35mCuántos registros desde el inicio desea ver: \033[0m"))
    while vision < 1 or vision > (filas - inicio_Cont):
        print(f"\033[91m Debe ser entre 1 y {filas - inicio_Cont}\033[0m")
        vision = int(input("\033[35mCuántos registros desde el inicio deseas ver: \033[0m"))

    fin= inicio_Cont+vision

    print(f"\033[32m{'-'*73}\033[0m")
    print(f"\033[32m{'IDs':<8}  {'ID Usuario':<13}\033  \033[35m{'Ubicación':>10}\
            {'ID Show':>12}\033[0m  \033[34m{'Precio':>14}\033[0m")
    print(f"\033[32m{'-'*73}\033[0m")

    for f in range(inicio_Cont, fin):
        print(f"\033[32m{matriz[f][0]:<8}  {matriz[f][1]:<13}\033[35m  {matriz[f][2]:>10}  {matriz[f][3]:>10}\033[0m  \033[34m{matriz[f][4]:>14}\033[0m")
# Función para mostrar matriz de shows con colores, espacios y encabezados
def ver_reserva():
    filas = 0
    try:
        with open("datos_reserva", "r", encoding="utf-8") as reservas:
            for linea in reservas:
                if linea.strip(): 
                    filas += 1
        
        if filas == 0:
            print("\033[93mEl archivo 'datos_reserva' está vacío. No hay nada que mostrar.\033[0m")

    except FileNotFoundError: 
        print(f"\033[31mError: No se pudo encontrar el archivo 'datos_reserva'.\033[0m")
    except OSError as e:
        print(f"\033[31mError de E/S al leer el archivo: {e}\033[0m")

    print(f"\033[36mTotal de reservas encontradas: {filas}\033[0m")
    inicio_Cont = int(input(f"\033[35mDesde qué reserva desea empezar (1 a {filas}): \033[0m"))
    
    while inicio_Cont < 1 or inicio_Cont > filas:
        print(f"\033[91mNúmero fuera de rango. Debe ser entre 1 y {filas}.\033[0m")
        inicio_Cont = int(input(f"\033[35mDesde qué reserva desea empezar: \033[0m"))

    max_vision = (filas - inicio_Cont + 1)
    vision = int(input(f"\033[35mCuántos registros desde el inicio desea ver (1 a {max_vision}): \033[0m"))
    
    while vision < 1 or vision > max_vision:
        print(f"\033[91mDebe ser entre 1 y {max_vision}\033[0m")
        vision = int(input(f"\033[35mCuántos registros desde el inicio deseas ver: \033[0m"))

    fin= inicio_Cont+vision

    print("\033[32m" + "-"*110 + "\033[0m")
    print(f"\033[36m{'IDS':<10}\033[0m \033[35m{'ID Usuario':<28}\033[0m \
    \033[32m{'ubicacion':>10}{'ID Show':>15}\033[0m \
    \033[34m{'PRECIO':>12}\033[0m")
    print("\033[32m" + "-" * 110 + "\033[0m")

    try:
        with open ("datos_reserva", "r", encoding="utf-8") as reservas:
            linea = reservas.readline().strip()
            
            while linea:
                try:

                    ids, ids_usuario, ubicacion, id_show, precio,numero_id = linea.split(";") 
                    num_id_actual = int(numero_id)                   
                    
                    if num_id_actual >= inicio_Cont and num_id_actual < fin:
                        print(f"\033[36m{id_show:<10}\033[0m \033[35m{ids:<28}\033[0m \
                        \033[32m{ids_usuario:>10}{ubicacion:>15}\033[0m \
                        \033[34m{id_show:>12}\033[0m \
                        \033[32m{precio:>20}\033[0m")

                except ValueError:
                    print(f"\033[31mLínea con formato incorrecto (se omite): {linea}\033[0m")
                
                linea = reservas.readline().strip()

    except OSError:
        print(f"\033[31mError: No se pudo abrir el archivo 'datos_show'.\033[0m")

    except OSError:
        print("no se pudo abrir el archivo")
