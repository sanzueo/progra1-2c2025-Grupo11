from nombres_teatroV2 import datos_globales, datos_globales_reserva, solo_ids_show,precios_show
from entidades.shows import ver_m, id_alt
from datetime import datetime
import random

def menu_shows(admin):
    if admin==False:
            usuario_i=int(input(
            "\n\033[92m=== MENÚ DE SHOWS ===         \033[0m\n"
            "\033[35m  → [1] VER SHOWS               \033[0m\n"
            "\033[35m  → [2] BUSCAR SHOWS            \033[0m\n"
            "\033[35m  → [3] VOLVER AL MENU PRINCIPAL\033[0m\n"
            "\033[1;35m Seleccione una opción: \033[0m" ))

    if admin==True:
            usuario_i=int(input(
            "\n\033[92m=== MENÚ DE SHOWS ===         \033[0m\n"
            "\033[35m  → [1] VER SHOWS               \033[0m\n"
            "\033[35m  → [2] BUSCAR SHOWS            \033[0m\n"
            "\033[35m  → [3] BORRAR SHOW             \033[0m\n"
            "\033[35m  → [4] EDITAR SHOW             \033[0m\n"
            "\033[35m  → [5] GENERAR SHOW            \033[0m\n"
            "\033[35m  → [6] VOLVER AL MENU PRINCIPAL\033[0m\n"
            "\033[1;35m Seleccione una opción: \033[0m" ))

    

    if usuario_i == 1:   #VER SHOW
        matriz_ordenada = sorted(datos_globales, key=lambda x: x[5])
        ver_m(matriz_ordenada)
    
    elif usuario_i == 2: #BUSCAR SHOW

        print("\033[35m\n1-BUSCAR POR ID\n2-BUSCAR POR FECHA\033[0m")

        elec = int(input(" "))

        if elec == 1:

            elec = int(input("\033[35mIngrese id: \033[0m"))

            lista_temp = []

            for i in datos_globales:
                if i[0] == elec:
                    lista_temp.append(i)

            if len(lista_temp) > 0:
                ver_m(lista_temp) 
            else:
                print("\033[31mNo coincide con ningún id.\033[0m")

        elif elec == 2:

            año = int(input("\033[35mIngrese año: \033[0m"))
            mes = int(input("\033[35mIngrese mes: \033[0m"))
            dia = int(input("\033[35mIngrese dia: \033[0m"))
            fecha_buscada = datetime(año, mes, dia).date()

            lista_temp = []

            for i in datos_globales:
                if i[5] == fecha_buscada:
                    lista_temp.append(i)


            if len(lista_temp) > 0:
                ver_m(lista_temp) 
            else:
                print("\033[31mNo hay fechas disponibles\033[0m")


    elif usuario_i == 3 and admin==True: #BORRAR SHOW
        eleccion = int(input("\033[4;35mIngrese id del show: \033[0m"))
        while eleccion not in solo_ids_show:
            print("\033[31mEl id ingresado no se encuentra en la base de datos\033[0m")
            eleccion = int(input("\033[35mIngrese nuevamente el id del show: \033[0m"))


        # Borrar el show
        for s in datos_globales[:]:
            if s[0] == eleccion:
                datos_globales.remove(s)

        # Borrar todas las reservas asociadas
        for r in datos_globales_reserva[:]:
            if r[3] == eleccion:
                datos_globales_reserva.remove(r)

        # Borrar todas las reservas asociadas
        for p in precios_show[:]:
            if p[0] == eleccion:
                precios_show.remove(p)

        # Actualizar lista de ids de shows
        solo_ids_show.clear()
        for s in datos_globales:
            solo_ids_show.append(s[0])
        print("\033[1;34mShow eliminado\033[0m")

    elif usuario_i == 4 and admin==True: #EDITAR SHOW

        eleccion = int(input("\033[1;35mSeleccione el id del show: \033[0m"))
        for i in datos_globales:
            if eleccion==i[0]:
                id_encontrado=True


        if id_encontrado==True:
            for i in datos_globales:
                eleccion==i[0]
            opcion = int(input(
                    "\n\033[92m=== MENÚ DE EDICIÓN ===      \033[0m\n"
                    "\033[35m  → [0] Editar tipo de evento  \033[0m\n"
                    "\033[35m  → [1] Editar duración        \033[0m\n"
                    "\033[35m  → [2] Editar todos los datos \033[0m\n"
                    "\033[1;35mSeleccione una opción: \033[0m"
                    ))
            while opcion not in (0, 1, 2, 3, 4):
                print("\033[91m Número fuera de rango.\033[0m")
                opcion = int(input(
                    "\n\033[92m=== MENÚ DE EDICIÓN ===      \033[0m\n"
                    "\033[35m  → [0] Editar tipo de evento  \033[0m\n"
                    "\033[35m  → [1] Editar duración        \033[0m\n"
                    "\033[35m  → [2] Editar todos los datos \033[0m\n"
                    "\033[1;35mSeleccione una opción: \033[0m"
                ))


            if opcion == 0:
                i[1] = input("\033[4;35mIngrese el nuevo tipo de evento: \033[0m")
                i[1]=i[1].ljust(20, " ")

            elif opcion == 1:
                fecha = i[5]

                suma = 0

                for u in datos_globales:
                    if u[5] == fecha:
                        suma +=u[2]

                if suma <= 750:
                    suma_aux = int(input("\033[35mIngresa la cantidad de minutos: \033[0m"))
                    while (suma + suma_aux) >= 750:
                        suma_aux = int(input("\033[35mIngresa la cantidad de minutos: \033[0m"))
                    i[2] = suma_aux
                    
                else:
                    print("\033[31mNo es posible editar la duracion del show.\033[0m")

            elif opcion == 2:

                i[1] = input("\033[4;35mIngrese el nuevo tipo de evento: \033[0m")
                i[1]=i[1].ljust(20, " ")
                fecha = i[5]

                suma = 0

                for u in datos_globales:
                    if u[5] == fecha:
                        suma +=u[2]

                if suma <= 750:
                    suma_aux = int(input("\033[35mIngrese la cantidad de minutos: \033[0m"))
                    while (suma + suma_aux) >= 750:
                        print("\033[31mExceso de minutos en el dia, ingrese un valor menor.\033[0m")
                        suma_aux = int(input("\033[35mIngrese la cantidad de minutos: \033[0m"))
                    i[2] = suma_aux
                    
                else:
                    print("\033[31mNo es posible editar la duracion del show.\033[0m")
            print("\033[1;34mShow editado con exito.\033[0m")

        elif eleccion != i[0]:
            print("\033[31mid no encontrado\033[0m")
            eleccion = int(input("\033[1;35mSeleccione el id del show: \033[0m"))
            
        ver_m(datos_globales)
    elif usuario_i == 5 and admin==True: #GENERAR SHOW
        id_show = id_alt()

        tipo_Evento = input("\033[35mIngrese el tipo de evento: \033[0m")
        tipo_Evento=tipo_Evento.ljust(20, " ")

        duracion = int(input("\033[35mIngrese la duracion del evento: \033[0m"))

        espectadores = 0

        espacios_disponibles = 999


        año = int(input("\033[35mIngrese año: \033[0m"))
        mes = int(input("\033[35mIngrese mes: \033[0m"))
        dia = int(input("\033[35mIngrese dia: \033[0m"))
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

            id_Act = id_show
            precio_b = random.randint(7200,12000)
            precio_b2 = precio_b * 2
            precio_b3 = precio_b * 3
            precios_show.append([id_Act,precio_b,precio_b2,precio_b3])
            

            print("\033[1;34mshow creado con exito\033[0m")   
             
        else:
            print("\033[31mNo hay espacio en el dia para el show ingresado.\033[0m")
        


    elif usuario_i==6 and admin==True or usuario_i==3 and admin==False:
        return -1