from nombres_teatroV2 import datos_globales, datos_globales_reserva, solo_ids_show
from entidades.shows import ver_m, id_alt
from datetime import datetime
import random

def menu_shows(admin):
    if admin==False:
            usuario_i=(input(
            "\n\033[92m=== MENÚ DE SHOWS ===         \033[0m\n"
            "\033[35m  → [1] VER SHOWS               \033[0m\n"
            "\033[35m  → [2] BUSCAR SHOWS            \033[0m\n"
            "\033[35m  → [3] VOLVER AL MENU PRINCIPAL\033[0m\n"
            "\033[1;35m Seleccione una opción:       \033[0m" ))

    if admin==True:
            usuario_i=(input(
            "\n\033[92m=== MENÚ DE SHOWS ===         \033[0m\n"
            "\033[35m  → [1] VER SHOWS               \033[0m\n"
            "\033[35m  → [2] BUSCAR SHOWS            \033[0m\n"
            "\033[35m  → [3] BORRAR SHOW             \033[0m\n"
            "\033[35m  → [4] EDITAR SHOW             \033[0m\n"
            "\033[35m  → [5] GENERAR SHOW            \033[0m\n"
            "\033[35m  → [6] VOLVER AL MENU PRINCIPAL\033[0m\n"
            "\033[1;35m Seleccione una opción:       \033[0m" ))

    

    if usuario_i == 1:   #VER SHOW
        matriz_ordenada = sorted(datos_globales, key=lambda x: x[5])
        ver_m(matriz_ordenada)
    
    elif usuario_i == 2: #BUSCAR SHOW

        print("\n1-BUSCAR POR ID\n2-BUSCAR POR FECHA")

        elec = int(input(" "))

        if elec == 1:

            elec = int(input("Ingrese id: "))

            lista_temp = []

            for i in datos_globales:
                if i[0] == elec:
                    lista_temp.append(i)

            if len(lista_temp) > 0:
                ver_m(lista_temp) 
            else:
                print("No coincide con ningún id.")

        elif elec == 2:
        
            año = int(input("Ingrese año"))
            mes = int(input("Ingrese mes"))
            dia = int(input("Ingrese dia: "))
            fecha_buscada = datetime(año, mes, dia).date()

            lista_temp = []

            for i in datos_globales:
                if i[5] == fecha_buscada:
                    lista_temp.append(i)


            if len(lista_temp) > 0:
                ver_m(lista_temp) 
            else:
                print("No hay fechas disponibles")


    elif usuario_i == 3 and admin==True: #BORRAR SHOW
        eleccion = int(input("Ingrese id del show: "))

        # Borrar el show
        for s in datos_globales[:]:
            if s[0] == eleccion:
                datos_globales.remove(s)

        # Borrar todas las reservas asociadas
        for r in datos_globales_reserva[:]:
            if r[3] == eleccion:
                datos_globales_reserva.remove(r)

        # Actualizar lista de ids de shows
        solo_ids_show.clear()
        for s in datos_globales:
            solo_ids_show.append(s[0])
        print("Show eliminado")

    elif usuario_i == 4 and admin==True: #EDITAR SHOW

        eleccion = int(input("Seleccione el id del show: "))

        for i in datos_globales:

            if i[0] == eleccion:
                i[1] = input("Seleccione porque tipo de evento quiere cambiarlo: ")

                fecha = i[5]

                suma = 0

                for u in datos_globales:
                    if u[5] == fecha:
                        suma +=u[2]

                if suma <= 750:
                    suma_aux = int(input("Ingresa la cantidad de minutos: "))
                    while (suma + suma_aux) >= 750:
                        suma_aux = int(input("Ingresa la cantidad de minutos: "))
                    i[2] = suma_aux
                    
                else:
                    print("No es posible agregar un show")
                
                i[3] = input("Seleccion la cant espectadores: ")

                i[4] = input("Seleccion la cant esp disponibles: ")
    elif usuario_i == 5 and admin==True: #GENERAR SHOW
        id_show = id_alt()

        tipo_Evento = input("Ingrese el tipo de evento: ")
        tipo_Evento=tipo_Evento.ljust(20, " ")

        duracion = int(input("Ingrese la duracion del evento: "))

        espectadores = int(input("Ingrese la capacidad maxima de espectadores: "))

        espacios_disponibles = random.randint(0,20)


        año = int(input("Ingrese año: "))
        mes = int(input("Ingrese mes: "))
        dia = int(input("Ingrese dia: "))
        fecha = datetime(año, mes, dia).date()

        #comprobar si se pasan los minuts

        lista_temp = []

        for i in datos_globales:
            if i[5] == fecha:
                lista_temp.append(i)

        suma = 0
        columna = 2
        for f in lista_temp:
            suma += f[columna]
        
        if (suma + duracion) < 720:

            datos_globales.append([id_show,tipo_Evento,duracion,espectadores,espacios_disponibles,fecha])
        else:
            print("No hay espacio en el dia para el show ingresado.")

    elif usuario_i==6 and admin==True or usuario_i==3 and admin==False:
        return -1