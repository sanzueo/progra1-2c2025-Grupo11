from nombres_teatroV2 import *
from ingreso import *
from entidades import *
from opciones_usuarios import *
from opciones_shows import *
from opciones_reservas import *

inicio = True
start = True

while start:
    while inicio == True:
        ingreso_op = menu_login()

        if ingreso_op == 0:
            log = login()
            if log == "ADMIN":
                admin = True
                menu = True
                inicio = False
            elif log == "Usuario":
                admin = False
                menu = True
                inicio = False
        elif ingreso_op == 1:
            ingr = registrar()

    # PROGRAMA PRINCIPAL
    while menu == True:
        print("\n1-Shows\n2-Reserva\n3-Usuario\n4-Cerrar sesion\n5-SALIR")
        usuario = int(input("Elige una opcion: "))

        # SUBMENÚS
        if usuario == 1:
            menu_shows(admin)

        elif usuario == 2:
            menu_reservas(admin)

        elif usuario == 3:
            menu_usuarios(admin)

        elif usuario == 4:  # CERRAR SESION
            admin = False
            inicio = True
            menu = False

        elif usuario == 5:  # SALIR
            menu = False
            start = False
