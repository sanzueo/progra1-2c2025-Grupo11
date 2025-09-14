"""
from datetime import datetime
from nombres_teatroV2 import datos_globales_reserva, datos_globales_usuarios, ids_shows, datos_globales


def menu_estadisticas():
    print
    usuario_i = int(input(
          "\033[92m=== MENÚ DE ESTADÍSTICAS ===                 \033[0m\n"
          "\033[35m  → [1] SHOWS MÁS VENDIDOS                   \033[0m\n"
          "\033[35m  → [2] USUARIOS ACTVIOS                     \033[0m\n"
          "\033[35m  → [3] SHOW MAS RECAUDADOS                  \033[0m\n"
          "\033[35m  → [4] USUARIOS CON MAS RESERVAS            \033[0m\n"
          "\033[35m  → [5] MES CON MAS RECAUDACION              \033[0m\n"
          "\033[35m  → [6] VOLVER                               \033[0m\n"
          "\033[1;35m Seleccione una opción:                    \033[0m" ))
    if usuario_i == 1:
        estadistica_shows_mas_vendidos()
    elif usuario_i == 2:
        estadistica_mas_user_activos()
    elif usuario_i == 3:
        shows_mas_recaudados()
    elif usuario_i == 4:
        usuarios_con_mas_re()
    elif usuario_i == 5:
        mes_con_mas_re()
    elif usuario_i == 6:
        return
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
    

def estadistica_mas_user_activos():
    #print("\n\033[92m=== RESERVAS MÁS REALIZADAS ===         \033[0m\n")
    
    lista_act = 0
    lista_in = 0
    
    
    for i in datos_globales_usuarios:
        if i[5] == True:
            lista_act += 1
        elif i[5] == False:
            lista_in += 1
    
    crear_Grafico(lista_act,lista_in)

            


    # Ordenar las reservas por la cantidad en orden descendente
    #sorted_reservas = sorted(reserva_count.items(), key=lambda x: x[1], reverse=True)

    #print("\033[1;35m Reserva ID     Cantidad \033[0m")
    #print("-------------------------------------")
   # for reserva_id, count in sorted_reservas:
        #print(f" {reserva_id}           {count}")
    #print("-------------------------------------\n")
    #menu_estadisticas()


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


def usuarios_con_mas_re():
    datos = []  # [[usuario_id, cantidad]]

    for i in datos_globales_reserva:
        usuario_id = i[1]
        encontrado = False

        for k in range(len(datos)):
            if datos[k][0] == usuario_id:
                datos[k][1] += 1
                encontrado = True

        if not encontrado:  
            datos.append([usuario_id, 1])  # 👈 acá estaba el error (antes ponías `datos` en lugar de `1`)

    print("Suma de reservas por usuario:")
    for g in datos:
        print("Usuario", g[0], "→", g[1])


def mes_con_mas_re():
    datos = []  

    for i in datos_globales: 
        fecha= i[5] 
        mes_num = fecha.month

        encontrado = False
        for k in range(len(datos)):
            if datos[k][0] == mes_num:  
                datos[k][1] += 1        
                encontrado = True
                break

        if not encontrado:
            datos.append([mes_num, 1])

    print("Suma de reservas por mes:")
    for g in datos:
        print("Mes", g[0], "→", g[1])

        



                

        





def crear_Grafico(num, num2):
    # Torre izquierda
    hola = []
    c = 0
    while c < num:
        if c == 0:
            hola.append("   _______")
        else:
            hola.append("  |       |")
        c += 1

    # Torre derecha
    hola2 = []
    c2 = 0
    while c2 < num2:
        if c2 == 0:
            hola2.append("   _______")
        else:
            hola2.append("  |       |")
        c2 += 1

    # Alinear ABAJO: rellenar abajo con líneas vacías
    alto = max(len(hola), len(hola2))
    while len(hola) < alto:
        hola.insert(0, "")   # línea vacía arriba izquierda
    while len(hola2) < alto:
        hola2.insert(0, "")  # línea vacía arriba derecha

    # Imprimir lado a lado sin gap extra

    print(f"      {num}          {num2}")

    for i in range(alto):
        print(hola[i].ljust(12) + hola2[i])



# PROGRAMA PRINCIPAL

def main():
    menu_estadisticas()

"""


from datetime import datetime
from nombres_teatroV2 import datos_globales_reserva, datos_globales_usuarios, ids_shows, datos_globales


def menu_estadisticas():
    usuario_i = int(input(
        "\033[92m=== MENÚ DE ESTADÍSTICAS ===                 \033[0m\n"
        "\033[35m  → [1] SHOWS MÁS VENDIDOS                   \033[0m\n"
        "\033[35m  → [2] USUARIOS ACTIVOS                     \033[0m\n"
        "\033[35m  → [3] SHOWS MÁS RECAUDADOS                 \033[0m\n"
        "\033[35m  → [4] USUARIOS CON MÁS RESERVAS            \033[0m\n"
        "\033[35m  → [5] MES CON MÁS RECAUDACIÓN              \033[0m\n"
        "\033[35m  → [6] VOLVER                               \033[0m\n"
        "\033[1;35m Seleccione una opción:                      \033[0m"
    ))

    if usuario_i == 1:
        estadistica_shows_mas_vendidos()
    elif usuario_i == 2:
        estadistica_mas_user_activos()
    elif usuario_i == 3:
        shows_mas_recaudados()
    elif usuario_i == 4:
        usuarios_con_mas_re()
    elif usuario_i == 5:
        mes_con_mas_re()
    elif usuario_i == 6:
        return
    else:
        print("\033[91mOpción no válida\033[0m")
        menu_estadisticas()


# 1. Shows más vendidos
def estadistica_shows_mas_vendidos():
    sorted_shows = sorted(datos_globales, key=lambda x: x[3], reverse=True)

    cantidad = int(input("Seleccione cuántos quiere ver (máximo 5): "))
    while cantidad > 5:
        print("Cantidad inválida, el máximo es 5")
        cantidad = int(input("Seleccione cuántos quiere ver (máximo 5): "))

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


# 2. Usuarios activos vs inactivos
def estadistica_mas_user_activos():
    lista_act = sum(1 for i in datos_globales_usuarios if i[5] is True)
    lista_in = sum(1 for i in datos_globales_usuarios if i[5] is False)
    crear_Grafico(lista_act, lista_in)


# 3. Shows más recaudados
def shows_mas_recaudados():
    recaudacion = {}  
    for fila in datos_globales_reserva:
        id_show, precio = fila[3], fila[4]
        recaudacion[id_show] = recaudacion.get(id_show, 0) + precio

    print("\n\033[92m=== RECAUDACIÓN POR SHOW ===\033[0m")
    for show, total in recaudacion.items():
        print("Show", show, "→", total)


# 4. Usuarios con más reservas
def usuarios_con_mas_re():
    reservas = {}  
    for fila in datos_globales_reserva:
        usuario_id = fila[1]
        reservas[usuario_id] = reservas.get(usuario_id, 0) + 1

    print("\n\033[92m=== RESERVAS POR USUARIO ===\033[0m")
    for usuario, total in reservas.items():
        print("Usuario", usuario, "→", total)


# 5. Mes con más recaudación
def mes_con_mas_re():
    recaudacion_por_mes = {}  
    for fila in datos_globales:
        fecha = fila[5]  
        mes = fecha.month
        precio = fila[4] if len(fila) > 4 else 0  
        recaudacion_por_mes[mes] = recaudacion_por_mes.get(mes, 0) + precio

    print("\n\033[92m=== RECAUDACIÓN POR MES ===\033[0m")
    for mes, total in recaudacion_por_mes.items():
        print("Mes", mes, "→", total)


# Gráfico simple 
def crear_Grafico(num, num2):
    hola = []
    for c in range(num):
        hola.append("   _______" if c == 0 else "  |       |")

    hola2 = []
    for c2 in range(num2):
        hola2.append("   _______" if c2 == 0 else "  |       |")

    alto = max(len(hola), len(hola2))
    while len(hola) < alto:
        hola.insert(0, "")
    while len(hola2) < alto:
        hola2.insert(0, "")

    print(f"      {num}          {num2}")
    for i in range(alto):
        print(hola[i].ljust(12) + hola2[i])


# Programa principal
def main():
    menu_estadisticas()
