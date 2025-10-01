from nombres_teatroV2 import *
from entidades.Usuarios import id_user
import re

#busqueda por dni y contraseña para revisar que esten en los datos globales de contraseña
def busqueda(dni, contraseña):
    for i in range(len(datos_de_ingreso_dni)):
        if datos_de_ingreso_dni[i] == dni and datos_globales_contraseñas[i] == contraseña:
            return True
    return False

#menu para el ingreso de forma coloreada
def menu_login():
# Marco verde brillante
    print("\033[92m╔════════════════════════════╗\033[0m")
    print("\033[92m║\033[0m       \033[93mMENÚ DE INGRESO\033[0m      \033[92m║\033[0m")
    print("\033[92m╠════════════════════════════╣\033[0m")

    # Opciones cyan
    print("\033[92m║\033[0m  \033[96m 0 → Iniciar Sesión\033[0m       \033[92m║\033[0m")
    print("\033[92m║\033[0m  \033[96m 1 → Registrarse\033[0m          \033[92m║\033[0m")

    # Cierre verde
    print("\033[92m╚════════════════════════════╝\033[0m")

    ingreso = input(f"\033[1;35m Seleccione una opción: \033[0m")
    #validacion de opciones
    while ingreso not in ("0", "1"):
        print(f"\033[91m Opción inválida, intente de nuevo.\033[0m")
        ingreso = input(f"\033[1;35m Seleccione una opción: \033[0m")

    return int(ingreso)

#parte de ingreso con contraseña y dni
def login():
    #ingreso de dni
    dni_ingres=int(input("\033[36m Escriba su dni para verificacion: \033[0m"))
    #revision del ingreso
    while dni_ingres not in datos_de_ingreso_dni and dni_ingres not in dni_admins:
        print("\033[91m Id no encontrado revise que este bien su dni.\033[0m")
        dni_ingres=int(input("\033[36m Escriba su dni para verificacion: \033[0m"))
    print()
    #ingreso de contraseña
    contraseña=input("\033[36m Escriba su contraseña de usuario: \033[0m")
    print()

    #revision de ambosal mismo tiempo
    while not (
        (dni_ingres in datos_de_ingreso_dni and contraseña in datos_globales_contraseñas) or
        (dni_ingres in dni_admins and contraseña in contraseñas_admin)
    ):
        #menu de reintento en caso de que no sean correctos alguno de ellos o no coincidan
        print("\033[91m DNI o contraseña incorrectos \033[0m")
        vuelta = int(input(
            "\n\033[92m=== MENÚ DE REINTENTO ===\033[0m\n"
            f"\033[35m  → [0] Volver al menú de ingreso\033[0m\n"
            "\033[35m  → [1] Reingresar el Dni\033[0m\n"
            "\033[35m  → [2] Reingresar la Contraseña\033[0m\n"
            "\033[1;35m Seleccione una opción: \033[0m"
        ))
        #validacion para que no elija otra opcion que no sea las indicadas
        while vuelta !=0 and vuelta!=1 and vuelta!=2:
            print("\033[91m DNI o contraseña incorrectos \033[0m")
            vuelta = int(input(
                "\n\033[92m=== MENÚ DE REINTENTO ===\033[0m\n"
                f"\033[35m  → [0] Volver al menú de ingreso\033[0m\n"
                "\033[35m  → [1] Reingresar el Dni\033[0m\n"
                "\033[35m  → [2] Reingresar la Contraseña\033[0m\n"
                "\033[1;35m Seleccione una opción: \033[0m"
            ))
        #sale de la funcion y te manda de nuevo al menu de ingreso
        if vuelta==0:
            return 
        #modificia el dni al que escriba el usuario
        elif vuelta==1:
            dni_ingres=int(input("\033[36m Escriba su dni para verificacion: \033[0m"))
        #modificia la contraseña a la que escriba el usuario
        elif vuelta==2:
            contraseña=(input("\033[36m Escriba su contraseña para verificacion: \033[0m"))

    #agarra el dni que escribio el usuario al iniciar sesion
    dni_en_uso.append(dni_ingres)

    
    #busca que las contraseñas de admin y el dni del admin esten en sus listas respectivas
    if contraseña in contraseñas_admin and dni_ingres in dni_admins:
        print("\033[92m Ingreso conseguido como ADMIN.\033[0m")
        return "ADMIN"
    #busca que coincidan el dni con la contraseña
    elif busqueda(dni_ingres, contraseña):
        print("\033[32m Ingreso conseguido como USUARIO.\033[0m")
        return "Usuario"

#registro
def registrar():
    #se asigna un id al usuario que se este registrando
    num_usuario = id_user()
    #el usuario escribe el nombre
    nombre = str(input("\033[36m Escriba el nombre que desee usar: \033[0m"))
    #el usuario escribe su dni 
    dni_cread = int(input("\033[36m Escriba el número de su DNI: \033[0m"))
    #validaciones basicas de dni debido a no poder acceder a una fuente confiable de dnis para comparar 
    while dni_cread < 0:
        print("\033[91m El DNI no puede ser negativo, intente de nuevo.\033[0m")
        dni_cread = int(input("\033[36m Escriba el número de su DNI: \033[0m"))

    #el usuario con numero de area
    telefono_cread = int(input("\033[36m Escriba su número de teléfono: \033[0m"))
    #revision de que sea dentro de los parametros asignados con el numero de area
    while telefono_cread < 1100000000 or telefono_cread > 1199999999:
        print("\033[91m Número no válido (1100000000 a 1199999999) \033[0m")
        telefono_cread = int(input("\033[36m Escriba su número de teléfono sin código de área: \033[0m")) 
    #convierte el telefono en un string
    telefono_cread=str(telefono_cread)
    #se define un patron
    patron= r"(11)(\d{6})(\d{2})"
    #se asigna una forma de como queremos mostrarlo
    numero_oculto=r"\1-XXXX-XX\3"
    #se substituye por los parametros asignados
    telefono_organizado=re.sub(patron,numero_oculto,telefono_cread)
    
    #el usuario escribe su email 
    email = input("\033[36m Escriba su email: \033[0m")
    #validaciones basicas de email
    arroba = re.findall('@', email)
    punto  = re.findall(r'\.', email)   

    if len(arroba) ==0 and len(punto) == 0:
        print("\033[91m Email inválido, debe contener '@' y '.' \033[0m")
        email = input("\033[36m Escriba su email: \033[0m")
    
    #el usuario define su contraseña    
    contraseña = input("\033[36m Escriba la contraseña que desea: \033[0m")

    #se muestra la informacion de una forma mas legible para la lectura del usuario
    print("\033[1;92m Usuario creado con éxito con la siguiente información:\033[0m")
    print(f"\033[92m \n",( "═" * 50),"\033[0m")
    print(f"\033[35m  - ID usuario : {num_usuario}\033[0m")
    print(f"\033[35m  - Nombre     : {nombre}\033[0m")
    print(f"\033[35m  - DNI        : {dni_cread}\033[0m")
    print(f"\033[35m  - Teléfono   : {telefono_organizado}\033[0m")
    print(f"\033[35m  - Email      : {email}\033[0m")
    print("\033[92m",( "═" * 50),"\033[0m")

    #se añaden los datos puestos por el usuario en sus respectivos lugares
    datos_de_ingreso_dni.append(dni_cread)
    datos_globales_contraseñas.append(contraseña)
    datos_globales_usuarios.append([num_usuario, nombre,dni_cread, telefono_cread, email, True])
    
    #se le dice al usuario que se a registrado con exito
    print("\033[1;36m Usuario registrado con éxito. \033[0m")
    print("")
