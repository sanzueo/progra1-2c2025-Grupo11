from nombres_teatroV2 import datos_globales_reserva, datos_globales,datos_globales_usuarios, dni_en_uso,precios_show, matriz_act
from entidades.reserva import ver_m2, id_alt_r, ver_busqueda_reserva
"""crear un archivo para los ids exclusivamente"""
from entidades.Usuarios import id_user
from entidades.shows import ver_m
from datetime import datetime

#se agarra el id del usuario comparandolo con el dni que esta en uso
def obt_id_Actual():
    #se agarra el dni en uso y se pone en otra variable
    dni_act = (dni_en_uso[0])
    #se crea una lista que es donde va a ir el usuario de ese dni
    user_act = []
    #se añade el id de ese usuario
    for i in datos_globales_usuarios:
        if i[2] == dni_act:
            user_act.append(i[0])

    return user_act[0]

#se inicia el menu de reservas
def menu_reservas(admin):
    
    colordorado="\033[38;2;207;181;59m"
    #se ponen las opciones que puede usar el usuario para que elija
    if admin==False:
        usuario_i = int(input(
            "\n\033[92m=== MENÚ DE RESERVA ===          \033[0m\n"
            "\033[35m  → [1] VER RESERVA                \033[0m\n"
            "\033[35m  → [2] GENERAR RESERVA            \033[0m\n"
            "\033[35m  → [3] VOLVER AL MENU DE OPCIONES \033[0m\n"
            "\033[1;35m Seleccione una opción: \033[0m"
            ))
    #se ponen las opciones que puede usar el admin para que elija (mas opciones debido a mayor autoridad) 
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

    #se muestra la reserva
    if usuario_i == 1:
        #se separa la vista de el admin y el no admin para diferenciar que es lo que pueden o no ver  
        if admin:
            #se muestra la matriz de las resrvas que hay
            ver_m2(datos_globales_reserva)
        
        #muestra las reservas que hizo ese usuario exclusivamente 
        elif admin == False:
            #se limpoia la lista para que si se agrega alguna se pueda actualizar
            matriz_act.clear()
            #se obtiene el id de usuario
            usuario_Act = obt_id_Actual()
            #se revisa que exista ese usuario en los datos de reservas y se añade a la lista
            for i in datos_globales_reserva:
                if int(i[1]) == usuario_Act:  
                    matriz_act.append(i)
            #si hay mas de una reserva te muestra la cantidad de reservas que hizo el usuario
            if len(matriz_act) > 0:
                ver_m2(matriz_act)
            #si no hay reservas te printea no hay reservas (no hay nada papu lince) anterioremente
            else:
                print("no hay ninguna reserva")


    #GENERAR RESERVA
    elif usuario_i == 2: 
        #se genera un id aleatorio
        id_reserva = id_alt_r() 
        #si no es un admin se busca el id del usuario
        if admin == False:
            id_usuario = obt_id_Actual()
        #si es admin se genera un id aleatorio
        else:
            id_usuario = id_user()
        #se muestran todos los shows
        ver_m(datos_globales) 
        
        busqueda = True
        
        while busqueda:
            #se pide un id para ver si puede o no entrar en ese show
            show = int(input("\033[35mIngrese el numero de id del show que desea asistir: \033[0m"))

            #se definen parametros booleanos para poder buscar si puede o no reservar ahi

            show_encontrado = False
            tiene_capacidad = False
            indice_show = -1
            
            #se revisa que tenga capacidad ademas de buscar si esta en la base de shows
            for i in range(len(datos_globales)):
                if datos_globales[i][0] == show:
                    show_encontrado = True
                    indice_show = i  
                    if datos_globales[i][4] > 0:
                        tiene_capacidad = True
            
            #se printea una cosa o la otra dependiendo de si no lo encuentra o no tiene capacidad
            if not show_encontrado:
                print("\033[31mEl id ingresado no existe, por favor ingrese un id valido.\033[0m")
            elif not tiene_capacidad:
                print("\033[31mEste show no tiene capacidad disponible.\033[0m")
            else:
                #se para la busqueda
                busqueda = False

        #se suma y resta los espectadores y los espacios disponibles 
        datos_globales[indice_show][4] -= 1  
        datos_globales[indice_show][3] += 1  

        ubicacion_u = int(input(
        "\n\033[92m=====  MENU DE UBICACIONES  =====\033[0m\n"
        "\n\033[35mPara Platea Seleccione 1:\033[0m\n"
        "\n\033[35mPara Campo Seleccione 2:\033[0m\n"
        f"\n\033[35m{colordorado}Para Vip Seleccione 3:\033[0m\n"
        "\n\033[92m=================================\033[0m\n"   
        "\n\033[35mElegi tipo de ubicación: \033[0m"))

        #validacion de is puso o no un numero correcto
        while ubicacion_u >3 or ubicacion_u <=0:
            print("\033[31mNumero inválido, por favor ingrese un numero válido.\033[0m")
            ubicacion_u = int(input(
            "\n\033[92m=====  MENU DE UBICACIONES  =====\033[0m\n"
            "\n\033[35mPara Platea Seleccione 1:\033[0m\n"
            "\n\033[35mPara Campo Seleccione 2:\033[0m\n"
            f"\n\033[35m{colordorado}Para Vip Seleccione 3:\033[0m\n"
            "\n\033[92m=================================\033[0m\n"   
            "\n\033[35mElegi tipo de ubicación: \033[0m"))

        #determina el precio basado en el show y el precio de dicho show
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
        print(f"\033[1;34mReserva generada con exito. El precio de su entrada termino en ${precio_act}\033[0m")
        
        #agrega los datos a la base de datos
        datos_globales_reserva.append([id_reserva, id_usuario, ubicacion_e, show, precio_act])
    #BUSQUEDA DE RESERVAS
    elif usuario_i == 3 and admin==True: 
        #crea una lista 
        reserva_enct = []
        
        #se crea un booleano para definir cuando se encuentra
        encontrado = False

        #se le dice que es lo que puede hacer
        eleccion = int(input("\033[35m → [1] BUSCAR RESERVA POR ID DE RESERVA\n → [2] BUSCAR RESERVA POR ID USUARIO\n\033[0m"))
        #agarra el caso numero 1
        if eleccion == 1:
            eleccion = int(input("\033[35mIngrese id de reserva: \033[0m"))
            
            #si lo encuentra lo añade a la lista 
            for i in datos_globales_reserva:
                if i[0] == eleccion:
                    encontrado = True
                    reserva_enct.append(i)
            
            #si no lo encuentra printea eso
            if not encontrado:
                print("\033[31mID de reserva no encontrada.\033[0m")
            else:
                #si lo encuentra muestra la reserva
                ver_busqueda_reserva(reserva_enct)
        
        #agarra el caso 2
        elif eleccion == 2:

            #se le indica que ponga su id de usuario
            eleccion = int(input("\033[35mIngrese ID de usuario: \033[0m"))

            #si lo encuentra lo añade a la lista
            for i in datos_globales_reserva:
                if i[1] == eleccion:
                    encontrado = True
                    reserva_enct.append(i)
            
            #si no lo encuentra printea esto
            if not encontrado:
                print("\033[31mID de usuario no encontrado.\033[0m")
            else:

                #si lo encuentra muestra la reservas que tiene ese usuario
                ver_busqueda_reserva(reserva_enct)

            

    #BORRAR RESERVA
    elif usuario_i == 4 and admin==False: 
        
        #agarra el id del usuario
        id_usuario=obt_id_Actual
        
        #se elimina la reserva de los datos globales 
        for i in datos_globales_reserva[:]:
            if i[1] == id_usuario:
                datos_globales_reserva.remove(i)
                #guarda el id para poder usarlo mas tarde para los espacios disponibles
                id_show.append(i[3])  

        #baja los espectadores y sube los espacios disponibles
        for i in datos_globales:
            if i[0] == id_show[0]:
                i[3] -= 1
                i[4] += 1
        
        #printea que la reserva fue eliminada
        print("\033[31mReserva eliminada.\033[0m")

    
    elif usuario_i == 4 and admin==True: #BORRAR RESERVA
        show_encontrado=False
        eleccion = int(input("\033[35mSeleccione id de reserva a eliminar: \033[0m"))
        for i in datos_globales_reserva:
            if i[0]==eleccion:
                show_encontrado=True
                print("\033[96mID de reserva confirmado.\033[0m")
        if not show_encontrado:
            print("\033[91mEsa reserva no es valida.\033[0m")
            eleccion = int(input("Seleccione ID de reserva a eliminar: "))

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
            print("\033[91mNo se encontró la reserva con ese ID.\033[0m")
        
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

                print("\033[91mOpción de ubicación no válida.\033[0m")

            print("\033[92mUbicación y precio actualizados correctamente.\033[0m")
        
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
                    print("\033[91mNo hay capacidad disponible en ese show.\033[0m")
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

                    print("\033[92mShow actualizado correctamente.\033[0m")
                
        else:
            print("\033[91mOpción no válida.\033[0m")


    elif usuario_i==6:
        return