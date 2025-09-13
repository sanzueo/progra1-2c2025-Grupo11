from nombres_teatroV2 import datos_globales_reserva, datos_globales_usuarios, ids_shows, datos_globales


def menu_estadisticas():
    print
    usuario_i = int(input(
          "\033[92m=== MENÚ DE ESTADÍSTICAS ===                 \033[0m\n"
          "\033[35m  → [1] SHOWS MÁS VENDIDOS                   \033[0m\n"
          "\033[35m  → [2] RESERVAS MÁS REALIZADAS              \033[0m\n"
          "\033[35m  → [3] SHOW MAS RECAUDADOS                  \033[0m\n"
          "\033[35m  → [4] VOLVER                               \033[0m\n"
          "\033[1;35m Seleccione una opción:                    \033[0m" ))
    if usuario_i == 1:
        estadistica_shows_mas_vendidos()
    elif usuario_i == 2:
        estadistica_reservas_mas_realizadas()
    elif usuario_i == 3:
        shows_mas_recaudados()
    elif usuario_i == 4:
        return
    elif usuario_i==4:
        estadisticas_activos()
    else:
        print("\033[91mOpción no válida\033[0m")
        menu_estadisticas()

def estadistica_shows_mas_vendidos():
    
    sorted_shows = sorted(datos_globales, key=lambda x: x[3], reverse=True)
    
    cantidad=int(input("seleccione cuantos quiere ver con un maximo de 5: "))
    while cantidad >5:
        print("cantidad invalida el maximo es 5")
        cantidad=int(input("seleccione cuantos quiere ver con un maximo de 5"))
    sorted_shows = sorted_shows[:cantidad]
    print("\n\033[92m=== SHOWS MÁS VENDIDOS ===         \033[0m\n")

        
    columnas_t = ["ids", "tipo evento", "duracion", "cant_e", "esp_d", "fecha"]
    anchos = [12, 20, 10, 8, 14, 14]

    print("-" * 74)
    print("".join(columnas_t[i].ljust(anchos[i]) for i in range(len(columnas_t))))
    print("-" * 74)

    for fila in sorted_shows:
        fila_str = [str(fila[i]).ljust(anchos[i]) for i in range(len(fila))]
        print("".join(fila_str))

def estadisticas_activos():
    A=0
    In=0
    for i in datos_globales_usuarios:

        if i[5]==True:
            A+=1
        if i[5]== False:
            In+=1
    print(f"hay {A} usuarios activos y {In} usuarios Inactivos")
    

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


def shows_mas_recaudados():
    

    #datos_globales_reserva.append([id_reserva, id_usuario, ubicacion_u, show,precio])


    agrupados = []

    for fila in datos_globales_reserva:
        id_show = fila[3]  
        precio = fila[4]    
        encontrado = False  


        for k in range(len(agrupados)):
            if agrupados[k][0] == id_show:
                agrupados[k][1] += precio
                encontrado = True  


        if not encontrado:
            agrupados.append([id_show, precio])


    print("Suma de precios por show:")
    for g in agrupados:
        print("Show", g[0], "→", g[1])




# PROGRAMA PRINCIPAL

def main():
    menu_estadisticas()

