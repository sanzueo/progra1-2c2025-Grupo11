from nombres_teatroV2 import *
from ingreso import *
from entidades.reserva import ver_m2, id_alt_r
from datetime import datetime
from entidades.shows import ver_m



matriz_act = []

def obt_id_Actual():

    dni_act = str(dni_en_uso[0])
    user_act = []


    for i in datos_globales_usuarios:
        if i[2] == dni_act:
            user_act.append(i[0])

    return user_act[0]



def menu_reservas(admin):
    if admin==False:
        print("\n1-Ver reserva\n2-Generar reserva")
    if admin==True:
        print("\n1-Ver reserva\n2-Generar reserva\n3-Buscar reserva\n4-Borrar reserva (falta acceso)\n5-Editar reserva")

    


    usuario_i = int(input("Elige una opcion: "))

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

        id_usuario= obt_id_Actual()
        
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

        ver_m(matriz) 
        show = int(input("Ingrese el numero de id del show que desea asistir: "))
        while show not in solo_ids_show:
            print("El id ingresado no existe, por favor ingrese un id valido.")
            show = int(input("Ingrese el numero de id del show que desea asistir: "))
        for i in datos_globales:
            if i[0] == show:
                i[4] = i[4] - 1
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
