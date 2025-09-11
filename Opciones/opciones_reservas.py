from nombres_teatroV2 import datos_globales_reserva, datos_globales, solo_ids_show,datos_globales_usuarios, dni_en_uso
from entidades.reserva import ver_m2, id_alt_r
"""crear un archivo para los ids exclusivamente"""
from entidades.Usuarios import id_user
from entidades.shows import ver_m
from datetime import datetime

def menu_reservas(admin):
    if admin==False:
        print("\n1-Ver reserva\n2-Generar reserva")
    if admin==True:
        print("\n1-Ver reserva\n2-Generar reserva\n3-Buscar reserva\n4-Borrar reserva (falta acceso)\n5-Editar reserva")
    usuario_i = int(input("Elige una opcion: "))

    if usuario_i == 1:  #ver reserva     
        ver_m2(datos_globales_reserva)

    elif usuario_i == 2: #GENERAR RESERVA

        id_reserva = id_alt_r()  # Llamar a la función

        """ dni_usuario = int(input("Ingresar el numero de id: "))
        while dni_usuario not in datos_de_ingreso_dni or dni_usuario not in id_usuarios:
            print("Id inexistente")
            dni_usuario = int(input("Ingresar el numero de id: ")) """
        
        
        for i in datos_globales_usuarios:
            if i[2] == dni_en_uso[0]:
                id_usuario = i[0]
        print("-----------------")
        print("Para platea elija 1")
        print("Para campo elija 2")
        print("Para vip elija 3")
        print("-----------------")

        ubicacion_u = int(input("Elegi tipo de ubiacion: "))
        while ubicacion_u >3 or ubicacion_u <=0:
            print("Numero invalido, por favor ingrese un numero valido.")
            ubicacion_u = int(input("Elegi tipo de ubiacion: "))
        if ubicacion_u == 1:
            ubicacion_e = "Platea   "
        elif ubicacion_u == 2:
            ubicacion_e = "Campo    "
        elif ubicacion_u == 3:
            ubicacion_e = "Vip       "

        ver_m(datos_globales) 
        show = int(input("Ingrese el numero de id del show que desea asistir: "))
        while show not in solo_ids_show:
            print("El id ingresado no existe, por favor ingrese un id valido.")
            show = int(input("Ingrese el numero de id del show que desea asistir: "))
        for i in datos_globales:
            if i[0] == show:
                i[4] = i[4] - 1
                if i[4] < 0:
                    print("No hay mas entradas disponibles para este show.")
                    i[4] = 0
                    show = int(input("Se agogaton las entadas, ingrese otro id:"))
                else:
                    print("Reserva realizada con exito.")

        datos_globales_reserva.append([id_reserva, id_usuario, ubicacion_e, show])

    elif usuario_i == 3: #BUSCAR RESERVA
    
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

    elif usuario_i == 4 and admin==True: #BORRAR RESERVA
        eleccion = int(input("Seleccione id de reserva a eliminar: "))


        for i in datos_globales_reserva[:]:
            if i[0] == eleccion:
                datos_globales_reserva.remove(i)
        print("Reserva eliminada")

    

    elif usuario_i == 5 and admin==True: #EDITAR RESERVA

        eleccion = int(input("Seleccione el id de reserva a editar: "))

        for i in datos_globales_reserva:
            if i[0] == eleccion:
                i[2] = int(input("Ingrese ubicacion: "))
                i[3] = input("Ingresar show: ")
