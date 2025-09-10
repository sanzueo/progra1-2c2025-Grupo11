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
    elif usuario_i == 2:  # EDITAR USUARIO
        for i in datos_globales_usuarios:
            if i[2] == dni_en_uso[0]:
                print("\033[96mSe ha accedido a su perfil\033[0m")
                opcion = int(input(
                    "\n\033[92m=== MENÚ DE EDICIÓN ===\033[0m\n"
                    "\033[35m  → [0] Editar nombre\033[0m\n"
                    "\033[35m  → [1] Editar teléfono\033[0m\n"
                    "\033[35m  → [2] Editar correo\033[0m\n"
                    "\033[1;35mSeleccione una opción: \033[0m"
                ))

                while opcion not in (0, 1, 2):
                    print("\033[91m Número fuera de rango.\033[0m")
                    opcion = int(input(
                        "\n\033[92m=== MENÚ DE EDICIÓN ===\033[0m\n"
                        "\033[35m  → [0] Editar nombre\033[0m\n"
                        "\033[35m  → [1] Editar teléfono\033[0m\n"
                        "\033[35m  → [2] Editar correo\033[0m\n"
                        "\033[1;35mSeleccione una opción: \033[0m"
                    ))

                if opcion == 0:
                    i[1] = input("\033[36mIngrese nombre: \033[0m")
                elif opcion == 1:
                    i[3] = int(input("\033[36mIngrese teléfono: \033[0m"))
                elif opcion == 2:
                    i[4] = input("\033[36mIngrese correo: \033[0m")

                print("\033[92mSe ha editado el usuario exitosamente.\033[0m")

    elif usuario_i == 2 and admin==True: #EDITAR USUARIO ADMIN
        eleccion = int(input("Seleccione el dni de usuario a editar: "))

        for i in datos_globales_usuarios:
                opcion = int(input(
                "\n\033[92m=== MENU DE EDICIÓN ===\033[0m\n"
                "\033[35m  → [0] Editar nombre\033[0m\n"
                "\033[35m  → [1] Editar DNI \033 [0m \n"
                "\033[35m  → [2] Editar telefono\033[0m\n"
                "\033[35m  → [3] Editar correo\033[0m\n"
                "\033[1;35m Seleccione una opción: \033[0m"
                ))
                while opcion not in (0, 1, 2):
                    print("\033 [91m Numero fuera de rango.\033[0m")
                    opcion = int(input(
                    "\n\033[92m=== MENÚ DE EDICIÓN ===\033[0m\n"
                    "\033[35m  → [0] Editar nombre\033[0m\n"
                    "\033[35m  → [1] Editar DNI \033 [0m \n"
                    "\033[35m  → [2] Editar telefono\033[0m\n"
                    "\033[35m  → [3] Editar correo\033[0m\n"
                    "\033[35m  → [4] Editar estado a Inactivo\033[0m\n"
                    "\033[35m  → [5] Editar estado a activo\033[0m\n"
                    "\033[1;35m Seleccione una opción: \033[0m"
                    ))
                if opcion == 0:
                    i[1] = input("\033[36m Ingrese nombre a cambiar: \033[0m")
                elif opcion == 1:
                    i[2] = input ("\033[36m ingrese el dni a cambiar: \033[0m")
                elif opcion == 2:
                    i[3] = int(input("\033[36m Ingrese el telefono a cambiar: \033[0m"))
                elif opcion == 3:
                    i[4] = input("\033[36m Ingrese el correo a cambiar: \033[0m")
                elif opcion == 4:
                    i[5]=False
                elif opcion == 5:
                    i[5] == True

    elif usuario_i == 3 and admin==True: #BORRAR USUARIO
        eleccion = int(input("Seleccione id a eliminar: "))
        print("\033[91m recuerde que esta accion es irrevertible \033[0m")
        print("\033[1;91 por favor vuelva a dar confirmacion\033[0m")
        opcion = int(input("\033[35m  → [4] Eliminar cuenta\033[0m\n"
            "\033[35m  → [2] Volver al menu\033[0m\n"
            f"\033[96m{"="*30}\033[0m\n"))
        for i in datos_globales_usuarios:
            if i[0] == eleccion:
                i[5] = False

        for i in datos_globales_reserva[:]:
            if i[1] == eleccion:
                datos_globales_reserva.remove(i)
