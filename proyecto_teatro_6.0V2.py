from ingreso import *
from Opciones.opciones_reservas import menu_reservas
from Opciones.opciones_usuarios import menu_usuarios
from Opciones.opciones_shows import menu_shows
from estadisticas import menu_estadisticas


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
                capture_data = False
            elif log == "Usuario":
                admin = False
                menu = True
                capture_data = False
        elif ingreso_nivel == 1:
            ingr = registrar()

    # PROGRAMA PRINCIPAL
    while menu == True:
        
        if admin==True:
            usuario =int(input(
                "\n\033[92m=== MENÚ DE OPCIONES ===\033[0m\n"
                "\033[35m  → [1] SHOWS             \033[0m\n"
                "\033[35m  → [2] RESERVAS          \033[0m\n"
                "\033[35m  → [3] USUARIOS          \033[0m\n"
                "\033[35m  → [4] ESTADISTICAS      \033[0m\n"
                "\033[35m  → [5] SALIR DE LA SESIÓN\033[0m\n"
                "\033[35m  → [6] SALIR DEL PROGRAMA\033[0m\n"
                "\033[1;35m Seleccione una opción: \033[0m"
            ))
        if admin==False:
            usuario =int(input(
                "\n\033[92m=== MENÚ DE OPCIONES ===\033[0m\n"
                "\033[35m  → [1] SHOWS             \033[0m\n"
                "\033[35m  → [2] RESERVAS          \033[0m\n"
                "\033[35m  → [3] USUARIOS          \033[0m\n"
                "\033[35m  → [4] SALIR DE LA SESIÓN\033[0m\n"
                "\033[35m  → [5] SALIR DEL PROGRAMA\033[0m\n"
                "\033[1;35m Seleccione una opción: \033[0m"
            ))


        # SUBMENÚS
        if usuario == 1:
            menu_shows(admin)
            if menu_shows==-1:
                usuario =int(input(
                "\n\033[92m=== MENÚ DE REINTENTO ===        \033[0m\n"
                "\033[35m  → [0] VOLVER AL MENÚ DE INGRESO  \033[0m\n"
                "\033[35m  → [1] REINGRESAR EL DNI          \033[0m\n"
                "\033[35m  → [2] REINGRESAR LA CONTRASEÑA   \033[0m\n"
                "\033[1;35m SELECCIONE UNA OPCION: \033[0m"
            ))
            
        elif usuario == 2:
            menu_reservas(admin)
            if menu_reservas==-1:
                usuario =int(input(
                        "\n\033[92m=== MENÚ DE OPCIONES ===\033[0m\n"
                        "\033[35m  → [1] SHOWS             \033[0m\n"
                        "\033[35m  → [2] RESERVAS          \033[0m\n"
                        "\033[35m  → [3] USUARIOS          \033[0m\n"
                        "\033[35m  → [4] SALIR DE LA SESIÓN\033[0m\n"
                        "\033[35m  → [5] SALIR DEL PROGRAMA\033[0m\n"
                        "\033[1;35m SELECCIONE UNA OPCION: \033[0m"
                    ))  
        elif usuario == 3: 
            menu_usuarios(admin)
            if menu_usuarios==-1:
                usuario =int(input(
                        "\n\033[92m=== MENÚ DE OPCIONES ===\033[0m\n"
                        "\033[35m  → [1] SHOWS             \033[0m\n"
                        "\033[35m  → [2] RESERVAS          \033[0m\n"
                        "\033[35m  → [3] USUARIOS          \033[0m\n"
                        "\033[35m  → [4] SALIR DE LA SESIÓN\033[0m\n"
                        "\033[35m  → [5] SALIR DEL PROGRAMA\033[0m\n"
                        "\033[1;35m SELECCIONE UNA OPCION: \033[0m"
                    ))
        elif usuario == 4 and admin==True:
            menu_estadisticas()

        elif usuario == 5 and admin ==True or usuario==4 and admin==False:  # CERRAR SESION
            admin = False
            capture_data = True
            menu = False
            dni_en_uso=[]

        elif usuario == 6 and admin==True or usuario==5 and admin==False:  # SALIR
            menu = False
            start = False
