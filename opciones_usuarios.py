from nombres_teatroV2 import *
from ingreso import *
from entidades import *

def menu_usuarios(admin):
    if admin==False:
        print("\n1-Ver usuario\n2-¿¿¿¿Editar usuario????")
    if admin==True:
        print("\n1-Ver usuario\n2-Editar usuario\n3-Borrar usuario")
    usuario_i = int(input("Elige una opcion: "))
    if usuario_i == 1: #VER USUARIOS
        ver_m3(matriz3) 
    elif usuario_i == 2: #EDITAR USUARIO
        print("gat")

        eleccion = int(input("Seleccione el id de usuario a editar: "))

        for i in datos_globales_usuarios:
            if i[0] == eleccion:
                i[1] = input("ingrese nombre: ")
                i[2] = int(input("Ingrese dni: "))
                i[3] = int(input("ingrese telefono: "))
                i[4] = input("Ingrese el correo: ")

    elif usuario_i == 3 and admin==True: #BORRAR USUARIO
        eleccion = int(input("Seleccione id a eliminar: "))

        for i in datos_globales_usuarios:
            if i[0] == eleccion:
                i[5] = False

        for i in datos_globales_reserva[:]:
            if i[1] == eleccion:
                datos_globales_reserva.remove(i)
