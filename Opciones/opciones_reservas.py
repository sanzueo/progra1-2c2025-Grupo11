from entidades import *
from nombres_teatroV2 import *
from datetime import datetime

def _ver_reservas():
    ver_m2(matriz2)

def _listar_shows_por_fecha():
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

def _borrar_reserva():
    eleccion = int(input("Seleccione id de reserva a eliminar: "))
    eliminado = False
    for i in datos_globales_reserva[:]:
        if i[0] == eleccion:
            datos_globales_reserva.remove(i)
            eliminado = True
    if eliminado:
        print("Reserva eliminada")
    else:
        print("No coincide con ningún id.")

def _generar_reserva_completa():
    id_reserva = id_alt_r()

    id_usuario = int(input("Ingresar el numero de id: "))
    while id_usuario not in datos_de_ingreso_dni:
        print("Id inexistente")
        id_usuario = int(input("Ingresar el numero de id: "))

    print("-----------------")
    print("Para platea elija 1")
    print("Para campo elija 2")
    print("Para vip elija 3")
    print("-----------------")

    ubicacion_u = int(input("Elegi tipo de ubicacion: "))
    while ubicacion_u > 3 or ubicacion_u <= 0:
        print("Numero invalido, por favor ingrese un numero valido.")
        ubicacion_u = int(input("Elegi tipo de ubicacion: "))

    if ubicacion_u == 1:
        ubicacion_e = "Platea   "
    elif ubicacion_u == 2:
        ubicacion_e = "Campo    "
    else:
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
    print("Reserva generada.")

def _editar_reserva():
    eleccion = int(input("Seleccione el id de reserva a editar: "))
    encontrado = False
    for i in datos_globales_reserva:
        if i[0] == eleccion:
            encontrado = True
            print("-----------------")
            print("Para platea elija 1")
            print("Para campo elija 2")
            print("Para vip elija 3")
            print("-----------------")
            ubicacion_u = int(input("Nueva ubicacion: "))
            while ubicacion_u not in (1, 2, 3):
                print("Numero invalido.")
                ubicacion_u = int(input("Nueva ubicacion: "))

            if ubicacion_u == 1:
                i[2] = "Platea   "
            elif ubicacion_u == 2:
                i[2] = "Campo    "
            else:
                i[2] = "Vip       "

            nuevo_show = int(input("Nuevo show (id): "))
            if nuevo_show in solo_ids_show:
                i[3] = nuevo_show
            else:
                print("ID de show inexistente, se mantiene el anterior.")
            print("Reserva editada.")
            break

    if not encontrado:
        print("No coincide con ningún id.")

def menu_reservas(admin: bool):
    # Un solo ciclo por llamada, como tu código original
    if admin == False:
        print("\n1-Ver reserva\n2-Generar reserva")
        usuario_i = int(input("Elige una opcion: "))

        if usuario_i == 1:
            _ver_reservas()
        elif usuario_i == 2:
            # Tu punto 2 original listaba shows por fecha
            _listar_shows_por_fecha()
        else:
            print("Opción inválida.")

    else:
        print("\n1-Ver reserva\n2-Generar reserva\n3-Borrar reserva\n4-Gererar reserva (pregunta)\n5-Editar reserva")
        usuario_i = int(input("Elige una opcion: "))

        if usuario_i == 1:
            _ver_reservas()
        elif usuario_i == 2:
            _listar_shows_por_fecha()
        elif usuario_i == 3:
            _borrar_reserva()
        elif usuario_i == 4:
            _generar_reserva_completa()
        elif usuario_i == 5:
            _editar_reserva()
        else:
            print("Opción inválida.")
