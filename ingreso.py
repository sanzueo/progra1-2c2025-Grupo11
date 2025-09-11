from nombres_teatroV2 import *
from entidades.Usuarios import id_user
import re


def busqueda(dni, contraseña):
    for i in range(len(datos_de_ingreso_dni)):
        if datos_de_ingreso_dni[i] == dni and datos_globales_contraseñas[i] == contraseña:
            return True
    return False

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

    while ingreso not in ("0", "1"):
        print(f"\033[91m Opción inválida, intente de nuevo.\033[0m")
        ingreso = input(f"\033[1;35m Seleccione una opción: \033[0m")

    return int(ingreso)

def login():
    dni_ingres=int(input("\033[36m Escriba su dni para verificacion: \033[0m"))
    while dni_ingres not in datos_de_ingreso_dni and dni_ingres not in dni_admins:
        print("\033[91m Id no encontrado revise que este bien su dni.\033[0m")
        dni_ingres=int(input("\033[36m Escriba su dni para verificacion: \033[0m"))

    print()
    contraseña=input("\033[36m Escriba su contraseña de usuario: \033[0m")
    print()

    while not (
        (dni_ingres in datos_de_ingreso_dni and contraseña in datos_globales_contraseñas) or
        (dni_ingres in dni_admins and contraseña in contraseñas_admin)
    ):
        print("\033[91m DNI o contraseña incorrectos \033[0m")
        vuelta = int(input(
            "\n\033[92m=== MENÚ DE REINTENTO ===\033[0m\n"
            f"\033[35m  → [0] Volver al menú de ingreso\033[0m\n"
            "\033[35m  → [1] Reingresar el Dni\033[0m\n"
            "\033[35m  → [2] Reingresar la Contraseña\033[0m\n"
            "\033[1;35m Seleccione una opción: \033[0m"
        ))

        while vuelta !=0 and vuelta!=1 and vuelta!=2:
            print("\033[91m DNI o contraseña incorrectos \033[0m")
            vuelta = int(input(
                "\n\033[92m=== MENÚ DE REINTENTO ===\033[0m\n"
                f"\033[35m  → [0] Volver al menú de ingreso\033[0m\n"
                "\033[35m  → [1] Reingresar el Dni\033[0m\n"
                "\033[35m  → [2] Reingresar la Contraseña\033[0m\n"
                "\033[1;35m Seleccione una opción: \033[0m"
            ))
        if vuelta==0:
            return 1  #habria que ver
        elif vuelta==1:
            dni_ingres=int(input("\033[36m Escriba su dni para verificacion: \033[0m"))
        elif vuelta==2:
            contraseña=(input("\033[36m Escriba su contraseña para verificacion: \033[0m"))

    dni_en_uso.append(dni_ingres)

    if contraseña in contraseñas_admin and dni_ingres in dni_admins:
        print("\033[92m Ingreso conseguido como ADMIN.\033[0m")
        return "ADMIN"
  
    elif busqueda(dni_ingres, contraseña):
        print("\033[32m Ingreso conseguido como USUARIO.\033[0m")
        return "Usuario"


def registrar():
    num_usuario = id_user()
    nombre = str(input("\033[36m Escriba el nombre que desee usar: \033[0m"))
    dni_cread = int(input("\033[36m Escriba el número de su DNI: \033[0m"))
    while dni_cread < 0:
        print("\033[91m El DNI no puede ser negativo, intente de nuevo\033[0m")
        dni_cread = int(input("\033[36m Escriba el número de su DNI: \033[0m"))

    telefono_cread = int(input("\033[36m Escriba su número de teléfono sin código de área: \033[0m"))
    while telefono_cread < 1100000000 or telefono_cread > 1199999999:
        print("\033[91m Número no válido (1100000000 a 1199999999) \033[0m")
        telefono_cread = int(input("\033[36m Escriba su número de teléfono sin código de área: \033[0m")) 
    telefono_cread=str(telefono_cread)
    patron= "[1]{2}-[0-9]{4}-[0-9]{4}"
    numero_oculto="11-XXXX-XXXX"
    telefono_organizado=re.sub(patron,numero_oculto,telefono_cread)


    email = input("\033[36m Escriba su email: \033[0m")
    coincidencias = re.findall("@", email)       
    if coincidencias==None:
        print("\033[36m Email inválido, debe ser @gmail.com, @hotmail.com o @yahoo.com \033[0m")
        email = input("\033[36m Escriba su email: \033[0m")

    contraseña = input("\033[36m Escriba la contraseña que desea: \033[0m")

    estado=True

    print("\033[1;92m Usuario creado con éxito con la siguiente información:\033[0m")
    print(f"\033[92m \n",( "═" * 50),"\033[0m")
    print(f"\033[35m  - ID usuario : {num_usuario}\033[0m")
    print(f"\033[35m  - Nombre     : {nombre}\033[0m")
    print(f"\033[35m  - DNI        : {dni_cread}\033[0m")
    print(f"\033[35m  - Teléfono   : {telefono_organizado}\033[0m")
    print(f"\033[35m  - Email      : {email}\033[0m")
    print("\033[92m",( "═" * 50),"\033[0m")
    
    #ajustes para su correctaa impresion 
    id_usuario = str(num_usuario).rjust(6)
    nombre = nombre.ljust(12)
    dni = str(dni_cread).rjust(8)
    telefono = str(telefono_cread).rjust(10)
    correo = email.ljust(25)

    datos_de_ingreso_dni.append(dni_cread)
    datos_globales_contraseñas.append(contraseña)
    datos_globales_usuarios.append([id_usuario, nombre, dni, telefono, correo, estado])

    print("\033[1;36m Usuario registrado con éxito \033[0m")
    print("")
"""testeo de las variables"""
#region testeo
"""

registrar()
login()

"""