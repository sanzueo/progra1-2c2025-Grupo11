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

        eleccion = int(input("Ingrese su dni de usuario: "))

        for i in datos_globales_usuarios:
            if i[0] == eleccion and eleccion == dni_en_uso:
                opcion = int(input(
                "\n\033[92m=== MENU DE EDICIÓN ===\033[0m\n"
                "\033[35m  → [0] Editar nombre\033[0m\n"
                "\033[35m  → [1] Editar telefono\033[0m\n"
                "\033[35m  → [2] Editar correo\033[0m\n"
                "\033[1;35m Seleccione una opción: \033[0m"
                ))
                while opcion not in (0, 1, 2):
                    print("Numero fuera de rango.")
                    opcion = int(input(
                    "\n\033[92m=== MENÚ DE EDICIÓN ===\033[0m\n"
                    "\033[35m  → [0] Editar nombre\033[0m\n"
                    "\033[35m  → [1] Editar telefono\033[0m\n"
                    "\033[35m  → [2] Editar correo\033[0m\n"
                    "\033[1;35m Seleccione una opción: \033[0m"
                    ))
                if opcion == 0:
                    i[1] = input("Ingrese nombre: ")
                elif opcion == 1:
                    i[3] = int(input("Ingrese telefono: "))
                elif opcion == 2:
                    i[4] = input("Ingrese el correo: ")
        print("Se ha editado el usuario exitosamente.")

    elif usuario_i == 2 and admin==True: #EDITAR USUARIO ADMIN
        eleccion = int(input("Seleccione el dni de usuario a editar: "))

        for i in datos_globales_usuarios:
            if i[0] == eleccion:
                i[1] = input("Ingrese nombre: ")
                i[2] = int(input("Ingrese dni: "))
                i[3] = int(input("Ingrese telefono: "))
                i[4] = input("Ingrese el correo: ")

    elif usuario_i == 3 and admin==True: #BORRAR USUARIO
        eleccion = int(input("Seleccione id a eliminar: "))

        for i in datos_globales_usuarios:
            if i[0] == eleccion:
                i[5] = False

        for i in datos_globales_reserva[:]:
            if i[1] == eleccion:
                datos_globales_reserva.remove(i)
