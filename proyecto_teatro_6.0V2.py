from ingreso import *
from Opciones.opciones_reservas import menu_reservas
from Opciones.opciones_usuarios import menu_usuarios
from Opciones.opciones_shows import menu_shows

capture_data = True
start = True



while start:
    while capture_data == True:
        ingreso_nivel = menu_login()

        if ingreso_nivel == 0:
            log = login()
            if log == "ADMIN":
                admin = True
                menu = True
                capture_data= False
            elif log == "Usuario":
                admin = False
                menu = True
                capture_data= False
        elif ingreso_nivel == 1:
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
            capture_data = True
            menu = False
            dni_en_uso=[]

        elif usuario == 5:  # SALIR
            menu = False
            start = False
