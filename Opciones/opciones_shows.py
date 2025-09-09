from entidades import *
from nombres_teatroV2 import *
from datetime import datetime
import random

def _recalcular_ids_shows():
    solo_ids_show.clear()
    for s in datos_globales:
        solo_ids_show.append(s[0])

def _ver_show():
    matriz_ordenada = sorted(datos_globales, key=lambda x: x[5])
    ver_m(matriz_ordenada)

def _buscar_show():
    print("\n1-BUSCAR POR ID\n2-BUSCAR POR FECHA")
    elec = int(input("Elige una opcion: "))
    if elec == 1:
        busc_id = int(input("Ingrese id: "))
        lista_temp = [i for i in datos_globales if i[0] == busc_id]
        if len(lista_temp) > 0:
            ver_m(lista_temp)
        else:
            print("No coincide con ningún id.")
    elif elec == 2:
        año = int(input("Ingrese año: "))
        mes = int(input("Ingrese mes: "))
        dia = int(input("Ingrese dia: "))
        fecha_buscada = datetime(año, mes, dia).date()
        lista_temp = [i for i in datos_globales if i[5] == fecha_buscada]
        if len(lista_temp) > 0:
            ver_m(lista_temp)
        else:
            print("No hay fechas disponibles.")
    else:
        print("Opción inválida.")

def _borrar_show():
    eleccion = int(input("Ingrese id del show: "))

    eliminado = False
    for s in datos_globales[:]:
        if s[0] == eleccion:
            datos_globales.remove(s)
            eliminado = True

    for r in datos_globales_reserva[:]:
        if r[3] == eleccion:
            datos_globales_reserva.remove(r)

    _recalcular_ids_shows()
    if eliminado:
        print("show eliminado")
    else:
        print("No coincide con ningún id.")

def _editar_show():
    eleccion = int(input("Seleccione el id del show: "))
    encontrado = False

    for i in datos_globales:
        if i[0] == eleccion:
            encontrado = True
            i[1] = input("seleccione porque tipo de evento quiere cambiarlo: ").ljust(20, " ")

            fecha = i[5]
            suma = 0
            for u in datos_globales:
                if u[5] == fecha:
                    suma += u[2]

            if suma <= 750:
                suma_aux = int(input("Ingresa la cantidad de minutos: "))
                while (suma + suma_aux) >= 750:
                    suma_aux = int(input("Ingresa la cantidad de minutos: "))
                i[2] = suma_aux
            else:
                print("No es posible agregar un show")

            i[3] = int(input("Seleccion la cant espectadores: "))
            i[4] = int(input("Seleccion la cant esp disponibles: "))
            print("Show editado.")
            break

    if not encontrado:
        print("No coincide con ningún id.")

def _generar_show():
    id_show = id_alt()

    tipo_Evento = input("Ingrese el tipo de evento: ").ljust(20, " ")
    duracion = int(input("Ingrese la duracion del evento: "))
    espectadores = int(input("Ingrese la capacidad maxima de espectadores: "))
    espacios_disponibles = random.randint(0, 20)

    año = int(input("Ingrese año: "))
    mes = int(input("Ingrese mes: "))
    dia = int(input("Ingrese dia: "))
    fecha = datetime(año, mes, dia).date()

    lista_temp = []
    for i in datos_globales:
        if i[5] == fecha:
            lista_temp.append(i)

    suma = 0
    for f in lista_temp:
        suma += f[2]

    if (suma + duracion) < 720:
        datos_globales.append([id_show, tipo_Evento, duracion, espectadores, espacios_disponibles, fecha])
        _recalcular_ids_shows()
        print("Show generado.")
    else:
        print("No hay espacio en el dia para el show ingresado.")

def menu_shows(admin: bool):
    # Un solo ciclo por llamada, como tu código original
    if admin == False:
        print("\n1-Ver show\n2-Buscar show")
        usuario_i = int(input("Elige una opcion: "))
        if usuario_i == 1:
            _ver_show()
        elif usuario_i == 2:
            _buscar_show()
        else:
            print("Opción inválida.")
    else:
        print("\n1-Ver show\n2-Buscar show\n3-Borrar show\n4-Editar show \n5-Generar show")
        usuario_i = int(input("Elige una opcion: "))
        if usuario_i == 1:
            _ver_show()
        elif usuario_i == 2:
            _buscar_show()
        elif usuario_i == 3:
            _borrar_show()
        elif usuario_i == 4:
            _editar_show()
        elif usuario_i == 5:
            _generar_show()
        else:
            print("Opción inválida.")
