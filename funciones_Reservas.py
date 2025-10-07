from nombres_teatroV2 import datos_globales_reserva, datos_globales,datos_globales_usuarios, dni_en_uso,precios_show, matriz_act
from entidades.reserva import ver_m2, id_alt_r, ver_busqueda_reserva
from entidades.Usuarios import id_user
from entidades.shows import ver_m
from datetime import datetime

#region por hacer
#hacer un modulo de colores o un diccionario con ellos
#ver la funcion de borrado y si queremos que se eliminen todas las reservas o solo las que decida ese usuario borrar
#en el caso de la segunda hace falrta validaciones sobre si la reserva es de el y asi
colordorado="\033[38;2;207;181;59m"


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

def vista_reserva(admin):
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

def generacion_reservas(admin):
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
        while ubicacion_u >3 or ubicacion_u <0:
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

def busqueda_Reserva():

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

def borrado_reserva(admin):
    #region se eliminan todas las reservas?
    """    
    if admin==False: 
            
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
    """
    #BORRAR RESERVA
    if admin==True: 
        
        #creamos un booleano para identificar cunado encuentre el show
        show_encontrado=False
        
        #se le pide el id del show para eliminarlo
        eleccion = int(input("\033[35mSeleccione id de reserva a eliminar: \033[0m"))
        
        #busca el show y cuenado lo encuentra el booleano se pone como true y se printea la confirmacion del id
        for i in datos_globales_reserva:
            if i[0]==eleccion:
                show_encontrado=True
                print("\033[96mID de reserva confirmado.\033[0m")
        
        #si no se encuentra la reserva se printea para 
        # que sepa que esa reserva no existe o no es valida y se le pide que lo vuelva a ingresar        
        if not show_encontrado:
            print("\033[91mEsa reserva no es valida.\033[0m")
            eleccion = int(input("Seleccione ID de reserva a eliminar: "))

        #se crea otra lista vacia
        id_show = []
        
        #busca por datos globales lo copia y lo remueve de 
        #datos globales reserva y mete el dato de show en el id_show para despues facilitar la busqueda
        for i in datos_globales_reserva[:]:
            if i[0] == eleccion:
                datos_globales_reserva.remove(i)
                id_show.append(i[3])
        
        #busca en id del show el show y si lo encuentra saca un espectador y agrega un espacio
        for i in datos_globales:
            if i[0] == id_show[0]:
                i[3] -= 1
                i[4] += 1
        
        
        print("\033[1;34mReserva eliminada con exito!\033[0m")
        
def edicion_reserva():        
        #se le muestra las reservas que hay para identificar el id mas rapidamente
        ver_m2(datos_globales_reserva)

        show_encontrado=False

        while show_encontrado == False:
            #se le pide que ingrese un id
            id_a_editar = int(input("\nSeleccione el ID de reserva a editar: "))
            #busca la reserva y si la encuentra se convierte reserva encontrada en esa reserva enteramente 
            for reserva in datos_globales_reserva:
                if reserva[0] == id_a_editar:  
                    reserva_encontrada = reserva
                    show_encontrado=True


            #si no lo encuentra se printe esto
            if show_encontrado==False:
                print("\033[91mNo se encontró la reserva con ese ID.\033[0m")
        
        #se printea esto para que sepas que id estas modificando
        print(f"\nEditando reserva ID: {reserva_encontrada[0]}")
        
        #se le pide que elija una opcion de edicion
        eleccion = int(input(
            "\n\033[92m=== MENÚ DE EDICIÓN DE RESERVA ===\033[0m\n"
            "\033[35m  → [1] EDITAR UBICACIÓN\033[0m\n"
            "\033[35m  → [2] EDITAR SHOW\033[0m\n"
            "\033[1;35mSeleccione una opción: \033[0m"
        ))
        
        #EDITAR UBICACIÓN
        if eleccion == 1:
            #si elije la opcion uno se le pide que ingrese a que ubicacion quiere pasar   
            ubicacion = int(input(
                "\n\033[92m=== SELECCIONE NUEVA UBICACIÓN ===\033[0m\n"
                "\033[35m  → [1] PLATEA\033[0m\n"
                "\033[35m  → [2] CAMPO\033[0m\n"
                "\033[35m  → [3] VIP\033[0m\n"
                "\033[1;35mSeleccione opción: \033[0m"
            ))
            
            #si no entra dentro de los numeros pedidos se le pide que ingrese nuevamente 
            #la ubicacion y se le indica que no es valida esa ubicacion
            while ubicacion !=1 and ubicacion !=2 and ubicacion !=3:
                print("\033[91mOpción de ubicación no válida.\033[0m")
                ubicacion = int(input(
                "\n\033[92m=== SELECCIONE NUEVA UBICACIÓN ===\033[0m\n"
                "\033[35m  → [1] PLATEA\033[0m\n"
                "\033[35m  → [2] CAMPO\033[0m\n"
                "\033[35m  → [3] VIP\033[0m\n"
                "\033[1;35mSeleccione opción: \033[0m"
                ))
            
            #depende de la ubicaion se le asigna un precio correspondiente con ese show y esa ubicacion
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



            print("\033[92mUbicación y precio actualizados correctamente.\033[0m")
    
        #EDITAR SHOW
        elif eleccion == 2:  
            
            #muestra todos los shows para que elijas nuevamente a que show queres ingresar para el cambio
            ver_m(datos_globales)

            #se busca el id del show y se pone un while para buscarlo
            validacion=True
            while validacion==True:
            #se le pide el id del show
                nuevo_show = int(input("\nIngrese el ID del nuevo show: "))
                
                #busca el show y si lo encuentra pone la variable como verdadera
                show_valido = False
                for show in datos_globales:
                    if show[0] == nuevo_show:
                        show_valido = True

                #si lo encuentra lo deja pasar y printea que si encontro el show
                if show_valido==True:
                    print("se a encontrado el show")
                    validacion=False

                elif show_valido==False:
                    print("\033[91mEl ID de show no existe\033[0m")


            for show in datos_globales:
                #se busca si hay o no disponibilidad en el show
                if show[0] == nuevo_show and show[4] < 0:
                    print("\033[91mNo hay capacidad disponible en ese show.\033[0m")
                
                #si lo hay se agrega una persona en los espectadores y uno menos en el espacio disponibles
                #y se le saca a el show antiguo del espectador
                elif show[0] == nuevo_show and show[4] > 0:
                    for show_viejo in datos_globales:
                        
                        #si ve que el show viejo coincide con el show de la reserva 
                        if show_viejo[0] == reserva_encontrada[3]:
                            show_viejo[4] += 1  
                            show_viejo[3] -= 1  
                    
                    show[4] -= 1  
                    show[3] += 1  
                
                    #se cambia el dato de el viejo show por el nuevo
                    reserva_encontrada[3] = nuevo_show  
                    
                    #se crea una variable que usa el strip para sacar los espacios y pasa los precios a ese otro show
                    ubicacion_actual = reserva_encontrada[2].strip()
                    print(ubicacion_actual)
                    
                    #cambia el precio basado en el show que se coloco y coordina con la ubicacion que tenia anteriormente
                    precios_cambio=0
                    while precios_cambio==0:
                        for precios in  precios_show:
                            if precios[0]==nuevo_show:
                                if ubicacion_actual=="platea":
                                    precios_cambio=precios[1]
                                elif ubicacion_actual=="campo":
                                    precios_cambio=precios[2]
                                elif ubicacion_actual=="vip":
                                    precios_cambio=precios[3]

                    #se cambia el precio por el del show en teoria
                    reserva_encontrada[4]=precios_cambio                  

                    print("\033[92mShow actualizado correctamente.\033[0m")


                
        #se le indica que puso una opcion invalida y pide que lo vuelvas a intentar        
        else:
            print("\033[91mOpción no válida.\033[0m")
            eleccion = int(input(
                "\n\033[92m=== MENÚ DE EDICIÓN DE RESERVA ===\033[0m\n"
                "\033[35m  → [1] EDITAR UBICACIÓN\033[0m\n"
                "\033[35m  → [2] EDITAR SHOW\033[0m\n"
                "\033[1;35mSeleccione una opción: \033[0m"
            ))

