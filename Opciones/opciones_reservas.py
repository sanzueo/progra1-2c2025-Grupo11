from nombres_teatroV2 import datos_globales_reserva, datos_globales, solo_ids_show,datos_globales_usuarios, dni_en_uso,precios_show
from entidades.reserva import ver_m2, id_alt_r
"""crear un archivo para los ids exclusivamente"""
from entidades.Usuarios import id_user
from entidades.shows import ver_m
from datetime import datetime


matriz_act = []

def obt_id_Actual():

    dni_act = (dni_en_uso[0])
    user_act = []


    for i in datos_globales_usuarios:
        if i[2] == dni_act:
            user_act.append(i[0])

    return user_act[0]



def menu_reservas(admin):
    if admin==False:
        usuario_i = int(input(
            "\n\033[92m=== MENÚ DE RESERVA ===          \033[0m\n"
            "\033[35m  → [1] VER RESERVA                \033[0m\n"
            "\033[35m  → [2] GENERAR RESERVA            \033[0m\n"
            "\033[35m  → [3] VOLVER AL MENU DE OPCIONES \033[0m\n"
            "\033[1;35m Seleccione una opción: \033[0m"
            ))
    if admin==True:
        usuario_i = int(input(
            "\n\033[92m=== MENÚ DE RESERVA ===         \033[0m\n"
            "\033[35m  → [1] VER RESERVA               \033[0m\n"
            "\033[35m  → [2] GENERAR RESERVA           \033[0m\n"
            "\033[35m  → [3] BUSCAR RESERVA            \033[0m\n"
            "\033[35m  → [4] BORRAR RESERVA            \033[0m\n"
            "\033[35m  → [5] EDITAR RESERVA            \033[0m\n"
            "\033[35m  → [6] VOLVER AL MENU DE OPCIONES\033[0m\n"
            "\033[1;35m Seleccione una opción: \033[0m"
        ))

    if usuario_i == 1:  #ver reserva
        if admin:     
            ver_m2(datos_globales_reserva)
        elif admin == False:

            matriz_act.clear()

            usuario_Act = obt_id_Actual()

            for i in datos_globales_reserva:
                if int(i[1]) == usuario_Act:  
                    matriz_act.append(i)

            if len(matriz_act) > 0:
                ver_m2(matriz_act)
                #ver_m2(matriz2)
                #ver_m3(matriz3)
            else:
                print("no hay nada papu lince")



    elif usuario_i == 2: #GENERAR RESERVA

        id_reserva = id_alt_r()  # Llamar a la función
        if admin==False:
            id_usuario= obt_id_Actual()
        if admin==True:
            id_usuario=id_alt_r()
        
        for i in datos_globales_usuarios:
            if i[2] == dni_en_uso[0]:
                id_usuario = i[0]
        

        

        ver_m(datos_globales) 
        show = int(input("Ingrese el numero de id del show que desea asistir: "))
        while show not in solo_ids_show:
            print("El id ingresado no existe, por favor ingrese un id valido.")
            show = int(input("Ingrese el numero de id del show que desea asistir: "))
            reserva_exitosa = False
            show_actual = show

            while not reserva_exitosa:
                show_encontrado = False
                tiene_capacidad = False
                lugar_del_show = -1
                
                for i in range(len(datos_globales)):
                    if datos_globales[i][0] == show_actual:
                        show_encontrado = True
                        lugar_del_show = i
                        if datos_globales[i][4] > 0:
                            tiene_capacidad = True
                
                if show_encontrado and tiene_capacidad:
                    datos_globales[lugar_del_show][4] -= 1
                    datos_globales[lugar_del_show][3] += 1
                    reserva_exitosa = True
                    print("Reserva realizada con éxito.")
                elif show_encontrado and not tiene_capacidad:
                    print("No hay entradas disponibles para este show.")
                    show_actual = int(input("Ingrese otro ID de show: "))
                else:
                    print("ID de show no encontrado.")
                    show_actual = int(input("Ingrese un ID de show válido: "))


        print("-----------------")
        print("Para platea elija 1")
        print("Para campo elija 2")
        print("Para vip elija 3")
        print("-----------------")

        ubicacion_u = int(input("Elegi tipo de ubicación: "))

        while ubicacion_u >3 or ubicacion_u <=0:
            print("Numero inválido, por favor ingrese un numero válido.")
            ubicacion_u = int(input("Elegi tipo de ubicación: "))
        if ubicacion_u == 1:
            ubicacion_e = "Platea   "
            for i in precios_show:
                if i[0] == show:
                    precio_act = i[1]

        elif ubicacion_u == 2:
            ubicacion_e = "Campo    "
            for i in precios_show:
                if i[0] == show:
                        precio_act = i[2]
        elif ubicacion_u == 3:
            for i in precios_show:
                ubicacion_e = "Vip       "
                if i[0] == show:
                        precio_act = i[3]
        print(f"reserva generada con exito el precio de su entrada termino en ${precio_act}")


    

        datos_globales_reserva.append([id_reserva, id_usuario, ubicacion_e, show,precio_act])

    elif usuario_i == 3 and admin==True: #BUSCAR RESERVA
    
        año = int(input("Ingrese año: "))
        mes = int(input("Ingrese mes: "))
        dia = int(input("Ingrese dia: "))
        fecha_buscada = datetime(año, mes, dia).date()

        lista_temp = []

        for i in datos_globales:
            if i[5] == fecha_buscada:
                lista_temp.append(i)


        if len(lista_temp) > 0:
            ver_m(lista_temp) 
        else:
            print("No hay fechas disponibles.")


    elif usuario_i == 4 and admin==False: #BORRAR RESERVA
        eleccion = int(input("Seleccione id de reserva a eliminar: "))
        

        for i in datos_globales_reserva[:]:
            if i[0] == eleccion:
                datos_globales_reserva.remove(i)
        print("Reserva eliminada")

    
    elif usuario_i == 4 and admin==True: #BORRAR RESERVA
        eleccion = int(input("Seleccione id de reserva a eliminar: "))


        for i in datos_globales_reserva[:]:
            if i[0] == eleccion:
                datos_globales_reserva.remove(i)
        print("Reserva eliminada")


    elif usuario_i == 5 and admin==True: #EDITAR RESERVA

        ver_m2(datos_globales_reserva)
        
        id_a_editar = int(input("\nSeleccione el ID de reserva a editar: "))

        for reserva in datos_globales_reserva:
            if reserva[0] == id_a_editar:  
                reserva_encontrada = reserva

        if not reserva_encontrada:
            print("\033[91mNo se encontró la reserva con ese ID\033[0m")
        
        print(f"\nEditando reserva ID: {reserva_encontrada[0]}")
        
        eleccion = int(input(
            "\n\033[92m=== MENÚ DE EDICIÓN DE RESERVA ===\033[0m\n"
            "\033[35m  → [1] EDITAR UBICACIÓN\033[0m\n"
            "\033[35m  → [2] EDITAR SHOW\033[0m\n"
            "\033[1;35mSeleccione una opción: \033[0m"
        ))
        
        if eleccion == 1:  # EDITAR UBICACIÓN
            ubicacion = int(input(
                "\n\033[92m=== SELECCIONE NUEVA UBICACIÓN ===\033[0m\n"
                "\033[35m  → [1] PLATEA\033[0m\n"
                "\033[35m  → [2] CAMPO\033[0m\n"
                "\033[35m  → [3] VIP\033[0m\n"
                "\033[1;35mSeleccione opción: \033[0m"
            ))
            
            if ubicacion == 1:
                reserva_encontrada[2] = "Platea   "
                for precio_info in precios_show:
                    if precio_info[0] == reserva_encontrada[3]:  
                        reserva_encontrada[4] = precio_info[1]  
                
            elif ubicacion == 2:
                reserva_encontrada[2] = "Campo    "
                for precio_info in precios_show:
                    if precio_info[0] == reserva_encontrada[3]:
                        reserva_encontrada[4] = precio_info[2]  

            elif ubicacion == 3:
                reserva_encontrada[2] = "Vip       "
                for precio_info in precios_show:
                    if precio_info[0] == reserva_encontrada[3]:
                        reserva_encontrada[4] = precio_info[3]  

                print("\033[91mOpción de ubicación no válida\033[0m")

            print("\033[92mUbicación y precio actualizados correctamente\033[0m")
        
        elif eleccion == 2:  # EDITAR SHOW
            ver_m(datos_globales)
            
            nuevo_show = int(input("\nIngrese el ID del nuevo show: "))

            show_valido = False
            for show in datos_globales:
                if show[0] == nuevo_show:
                    show_valido = True

            if not show_valido:
                print("\033[91mEl ID de show no existe\033[0m")

            
            for show in datos_globales:

                if show[0] == nuevo_show and show[4] < 0:
                    print("\033[91mNo hay capacidad disponible en ese show\033[0m")
                elif show[0] == nuevo_show and show[4] > 0:
                    for show_viejo in datos_globales:
                        if show_viejo[0] == reserva_encontrada[3]:
                            show_viejo[4] += 1  
                            show_viejo[3] -= 1  
                    
                    show[4] -= 1  
                    show[3] += 1  
                    
                    reserva_encontrada[3] = nuevo_show  
                    
                    
                    ubicacion_actual = reserva_encontrada[2].strip()
                    for precio_info in precios_show:
                        if precio_info[0] == nuevo_show:
                            if ubicacion_actual == "Platea":
                                reserva_encontrada[4] = precio_info[1]
                            elif ubicacion_actual == "Campo":
                                reserva_encontrada[4] = precio_info[2]
                            elif ubicacion_actual == "Vip":
                                reserva_encontrada[4] = precio_info[3]

                    print("\033[92mShow actualizado correctamente\033[0m")
                
        else:
            print("\033[91mOpción no válida\033[0m")


    elif usuario_i==6:
        return -1