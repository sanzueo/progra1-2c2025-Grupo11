#estadisticas

from nombres_teatroV2 import datos_globales_reserva, datos_globales_usuarios, ids_shows
from entidades.shows import ver_m

def menu_estadisticas():
    print("\n\033[92m=== MENÚ DE ESTADÍSTICAS ===         \033[0m\n"
          "\033[35m  → [1] SHOWS MÁS VENDIDOS         \033[0m\n"
          "\033[35m  → [2] RESERVAS MÁS REALIZADAS     \033[0m\n"
          "\033[35m  → [3] VOLVER                      \033[0m\n")
    usuario_i = int(input("\033[1;35m Seleccione una opción:       \033[0m" ))
    if usuario_i == 1:
        estadistica_shows_mas_vendidos()
    elif usuario_i == 2:
        estadistica_reservas_mas_realizadas()
    elif usuario_i == 3:
        return
    else:
        print("Opción no válida")
        menu_estadisticas()

def estadistica_shows_mas_vendidos():
    print("\n\033[92m=== SHOWS MÁS VENDIDOS ===         \033[0m\n")
    show_count = {}
    for reserva in datos_globales_reserva:
        show_id = reserva[2]  # Asumiendo que el ID del show está en la posición 2
        if show_id in show_count:
            show_count[show_id] += 1
        else:
            show_count[show_id] = 1

    # Ordenar los shows por la cantidad de reservas en orden descendente
    sorted_shows = sorted(show_count.items(), key=lambda x: x[1], reverse=True)

    print("\033[1;35m Show ID     Cantidad de Reservas \033[0m")
    print("-------------------------------------")
    for show_id, count in sorted_shows:
        print(f" {show_id}           {count}")
    print("-------------------------------------\n")
    menu_estadisticas()

def estadistica_reservas_mas_realizadas():
    print("\n\033[92m=== RESERVAS MÁS REALIZADAS ===         \033[0m\n")
    reserva_count = {}
    for reserva in datos_globales_reserva:
        reserva_id = reserva[0]  # Asumiendo que el ID de la reserva está en la posición 0
        if reserva_id in reserva_count:
            reserva_count[reserva_id] += 1
        else:
            reserva_count[reserva_id] = 1

    # Ordenar las reservas por la cantidad en orden descendente
    sorted_reservas = sorted(reserva_count.items(), key=lambda x: x[1], reverse=True)

    print("\033[1;35m Reserva ID     Cantidad \033[0m")
    print("-------------------------------------")
    for reserva_id, count in sorted_reservas:
        print(f" {reserva_id}           {count}")
    print("-------------------------------------\n")
    menu_estadisticas()

# PROGRAMA PRINCIPAL

def main():
    menu_estadisticas()

if __name__ == "__main__":
    main()
    capture_data = False
    inicio = False
    menu = True
    admin = False
    start = True
