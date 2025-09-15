from nombres_teatroV2 import datos_globales_reserva, datos_globales, solo_ids_show,datos_globales_usuarios, dni_en_uso,precios_show, ids_reserva
from entidades.reserva import ver_m2, id_alt_r, ver_busqueda_reserva
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

    colordorado="\033[38;2;207;181;59m"

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
        id_reserva = id_alt_r() 
        
        if admin == False:
            id_usuario = obt_id_Actual()
        else:
            id_usuario = id_user()
        ver_m(datos_globales) 
        
        busqueda = True
        show_encontrado = False
        tiene_capacidad = False
        indice_show = -1
        
        while busqueda:
            show = int(input("\033[35mIngrese el numero de id del show que desea asistir: \033[0m"))

            show_encontrado = False
            tiene_capacidad = False
            indice_show = -1
            

            for i in range(len(datos_globales)):
                if datos_globales[i][0] == show:
                    show_encontrado = True
                    indice_show = i  
                    if datos_globales[i][4] > 0:
                        tiene_capacidad = True
            
            if not show_encontrado:
                print("\033[31mEl id ingresado no existe, por favor ingrese un id valido.\033[0m")
            elif not tiene_capacidad:
                print("\033[31mEste show no tiene capacidad disponible.\033[0m")
            else:
                
                busqueda = False

        datos_globales[indice_show][4] -= 1  
        datos_globales[indice_show][3] += 1  
        print("\033[92m=====  MENU DE UBICACIONES  =====\033[0m")
        print("\033[35mPara Platea Seleccione 1:\033[0m")
        print("\033[35mPara Campo Seleccione 2:\033[0m")
        print(f"{colordorado}vip Seleccione 3:\033[0m")
        print("\033[92m=================================\033[0m")
    
        ubicacion_u = int(input("\033[35mElegi tipo de ubicación: \033[0m"))

        while ubicacion_u >3 or ubicacion_u <=0:
            print("\033[31mNumero inválido, por favor ingrese un numero válido.\033[0m")
            ubicacion_u = int(input("\033[35mElegi tipo de ubicación: \033[0m"))
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
        print(f"\033[1;34mreserva generada con exito el precio de su entrada termino en ${precio_act}\033[0m")


    

        datos_globales_reserva.append([id_reserva, id_usuario, ubicacion_e, show, precio_act])

    elif usuario_i == 3 and admin==True: #BUSCAR RESERVA

        print("\033[35m → [1] BUSCAR RESERVA POR ID DE RESERVA\n → [2] BUSCAR RESERVA POR ID USUARIO\033[0m")

        eleccion = int(input(""))

        if eleccion == 1:
            eleccion = int(input("\033[35mIngrese id de reserva: \033[0m"))

            reserva_enct = []

            encontrado = False

            for i in datos_globales_reserva:
                if i[0] == eleccion:
                    encontrado = True
                    reserva_enct.append(i)
            
            if not encontrado:
                print("\033[31mId Reserva no encontrada\033[0m")
            else:
                ver_busqueda_reserva(reserva_enct)

        elif eleccion == 2:
            eleccion = int(input("\033[35mIngrese id de usuario: \033[0m"))

            reserva_enct = []

            encontrado = False

            for i in datos_globales_reserva:
                if i[1] == eleccion:
                    encontrado = True
                    reserva_enct.append(i)
            
            if not encontrado:
                print("\033[31mId Usuario no encontrada\033[0m")
            else:
                ver_busqueda_reserva(reserva_enct)

            


    elif usuario_i == 4 and admin==False: #BORRAR RESERVA
        id_usuario=obt_id_Actual
        for i in datos_globales_reserva[:]:
            if i[1] == id_usuario:
                datos_globales_reserva.remove(i)
                id_show.append(i[3])  

        for i in datos_globales:
            if i[0] == id_show[0]:
                i[3] -= 1
                i[4] += 1
        print("\033[31mReserva eliminada\033[0m")

    
    elif usuario_i == 4 and admin==True: #BORRAR RESERVA
        show_encontrado=False
        eleccion = int(input("\033[35mSeleccione id de reserva a eliminar: \033[0m"))
        for i in datos_globales_reserva:
            if i[0]==eleccion:
                show_encontrado=True
                print("\033[96mid de reserva confirmado\033[0m")
        if not show_encontrado:
            print("\033[91mesa reserva no es valida\033[0m")
            eleccion = int(input("Seleccione id de reserva a eliminar: "))

        id_show = []

        for i in datos_globales_reserva[:]:
            if i[0] == eleccion:
                datos_globales_reserva.remove(i)
                id_show.append(i[3])
        

        for i in datos_globales:
            if i[0] == id_show[0]:
                i[3] -= 1
                i[4] += 1

        print("\033[1;34mReserva eliminada con exito!\033[0m")


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