from datetime import datetime
from nombres_teatroV2 import datos_globales_reserva, datos_globales_usuarios, ids_shows, datos_globales

#se inicia el menu de estadisticass
def menu_estadisticas():
    #se muestran las opciones que pueden elegir
    usuario_i = int(input(
        "\033[92m=== MENÚ DE ESTADÍSTICAS ===                 \033[0m\n"
        "\033[35m  → [1] SHOWS MÁS VENDIDOS                   \033[0m\n"
        "\033[35m  → [2] USUARIOS ACTIVOS                     \033[0m\n"
        "\033[35m  → [3] SHOWS MÁS RECAUDADOS                 \033[0m\n"
        "\033[35m  → [4] USUARIOS CON MÁS RESERVAS            \033[0m\n"
        "\033[35m  → [5] VOLVER                               \033[0m\n"
        "\033[1;35m Seleccione una opción: \033[0m"
    ))

    #depende de la opcion se habilita una o otra funcion para mostrar esa opcion
    if usuario_i == 1:
        estadistica_shows_mas_vendidos()
    elif usuario_i == 2:
        estadistica_mas_user_activos()
    elif usuario_i == 3:
        shows_mas_recaudados()
    elif usuario_i == 4:
        usuarios_con_mas_re()
    elif usuario_i == 5:
        return
    #se delimita las opciones que podes con esto para que si elije mal alguna opcion pueda volver a ver las opciones y elija bien
    else:
        print("\033[91mOpción no válida\033[0m")
        menu_estadisticas()


# 1. Shows más vendidos
def estadistica_shows_mas_vendidos():
    #se ordena datos globales por la contidad de espectadores 
    sorted_shows = sorted(datos_globales, key=lambda x: x[3], reverse=True)
    #se añade la funcion para que solo puedas ver un cantidad determinada menor a 5
    cantidad = int(input("Seleccione cuántos quiere ver (máximo 5): "))
    #validacion de que no sea mayor a 5
    while cantidad > 5:
        print("Cantidad inválida, el máximo es 5")
        cantidad = int(input("Seleccione cuántos quiere ver (máximo 5): "))
    
    #se aplica un corte a la matriz para que solo se muestre hasta ese punto     
    sorted_shows = sorted_shows[:cantidad]
    #se printea de una forma mas organizada usando anchos 
    print("\n\033[92m=== SHOWS MÁS VENDIDOS ===         \033[0m\n")

    columnas_t = ["ID's", "Tipo de evento", "Duración", "Cant. Espectadores", "Esp. Disponibles", "Fecha"]
    anchos = [12, 20, 10, 8, 14, 14]

    print("-" * 74)
    print("".join(columnas_t[i].ljust(anchos[i]) for i in range(len(columnas_t))))
    print("-" * 74)

    for fila in sorted_shows:
        fila_str = [str(fila[i]).ljust(anchos[i]) for i in range(len(fila))]
        print("".join(fila_str))


# 2. Usuarios activos vs inactivos
def estadistica_mas_user_activos():
    #se suman los usuarios para ver la cantidad de activos o inactivos
    lista_act = sum(1 for i in datos_globales_usuarios if i[5] is True)
    lista_in = sum(1 for i in datos_globales_usuarios if i[5] is False)

    #se crea otra variable que sea igual a las otras
    activo=lista_act
    inactivo=lista_in

    #se verifica que el grafico que vamos a ser sea dentro de limites razonables
    #en usuarios activos
    if lista_act <= 100:
        num_barras_act = lista_act // 10
    else:
        num_barras_act = lista_act // 10

    #en usuarios inactivos
    if lista_in <= 100:
        num_barras_in = lista_in // 10
    else:
        num_barras_in = lista_in // 10
    
    # Asegurar que haya al menos 1 barra si hay usuarios
    if lista_act > 0 and num_barras_act == 0:
        num_barras_act = 1
    if lista_in > 0 and num_barras_in == 0:
        num_barras_in = 1
    #se llama la funcion de creacion de graficos dandoles todos los datos
    crear_Grafico(num_barras_act, num_barras_in, activo, inactivo)


# 3. Shows más recaudados
def shows_mas_recaudados():
    #se crea un diccionario para las recaudaciones
    """
        recaudacion = {}  
        #agarra el show y el precio 
        for fila in datos_globales_reserva:
            id_show, precio = fila[3], fila[4]
            recaudacion[id_show] = recaudacion.get(id_show, 0) + precio

        print("\n\033[92m=== RECAUDACIÓN POR SHOW ===\033[0m")
        for show, total in recaudacion.items():
            print("Show", show, "→", "$", total)
    
    Falta ordenarlas por recaudacion
    """

# 4. Usuarios con más reservas
def usuarios_con_mas_re():
    """    #crea un diccionario
    reservas = {}  
    #agarra el id de usuario por cada reserva que tengas
    for fila in datos_globales_reserva:
        usuario_id = fila[1]
        reservas[usuario_id] = reservas.get(usuario_id, 0) + 1

    print("\n\033[92m=== RESERVAS POR USUARIO ===\033[0m")
    for usuario, total in reservas.items():
        print("Usuario", usuario, "→", total)

    falta organizarlos y poner un limite a la cantidad que muestre
    """

# Gráfico simple 
def crear_Grafico(num, num2, act, inac):
    #se crea una lista
    hola = []
    #por la cantidad de activos que haya se añade un append para simular un grafico
    for c in range(num):
        hola.append("   _______" if c == 0 else "  |       |")
    #por la cantidad de inactivos que haya se añade un append para simular un grafico
    hola2 = []
    for c2 in range(num2):
        hola2.append("   _______" if c2 == 0 else "  |       |")
    
    #se define un alto con el maximo de largo de ambas listas
    alto = max(len(hola), len(hola2))
    #se hace que si uno es mas largo que el otro se insetan espacios en el mas chico para que no se rompa el grafico
    while len(hola) < alto:
        hola.insert(0, "")
    while len(hola2) < alto:
        hola2.insert(0, "")
    
    #se printean los datos
    print(f'    {"ACTIVO"}     {"INACTIVO"}   ')
    print(f"      {act}          {inac}")
    for i in range(alto):
        print(hola[i].ljust(12) + hola2[i])

