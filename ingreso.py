from nombres_teatroV2 import *
from funciones_de_teatroV2 import *
import re



def menu_login():
# Marco verde brillante
    print("\033[92m╔════════════════════════════╗\033[0m")
    print("\033[92m║\033[0m       \033[93mMENÚ DE INGRESO\033[0m      \033[92m║\033[0m")
    print("\033[92m╠════════════════════════════╣\033[0m")

    # Opciones cyan
    print("\033[92m║\033[0m  \033[96m0 → Iniciar Sesión\033[0m        \033[92m║\033[0m")
    print("\033[92m║\033[0m  \033[96m1 → Registrarse\033[0m           \033[92m║\033[0m")

    # Cierre verde
    print("\033[92m╚════════════════════════════╝\033[0m")

    ingreso = input(f"\033[1;35m Seleccione una opción: \033[0m")
    while ingreso not in ("0", "1"):
        print(f"\033[91m Opción inválida, intente de nuevo.\033[0m")
        ingreso = input(f"\033[1;35m Seleccione una opción: \033[0m")

    return int(ingreso)

def login():
    dni_ingres=int(input("\033[36m escriba su dni para verificacion \033[0m"))
    while dni_ingres not in datos_de_ingreso_dni and dni_ingres not in dni_admins:
        print("\033[91m id no encontrado revise que este bien su dni\033[0m")
        dni_ingres=int(input("\033[36m escriba su dni para verificacion \033[0m"))

    print()
    contraseña=input("\033[36m escriba su contraseña de usuario: \033[0m")
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
            return "Fallo"  #habria que ver
        elif vuelta==1:
            dni_ingres=int(input("\033[36m escriba su dni para verificacion: \033[0m"))
        elif vuelta==2:
            contraseña=(input("\033[36m escriba su contraseña para verificacion: \033[0m"))



    if contraseña in contraseñas_admin and dni_ingres in dni_admins:
        print("\033[92m Ingreso conseguido como ADMIN\033[0m")
        return "ADMIN"
    elif busqueda(dni_ingres, contraseña):
        print("\033[96m Ingreso conseguido como USUARIO\033[0m")
        return "Usuario"


def registrar():
    num_usuario = id_user()
    nombre = str(input("Escriba el nombre que desee usar: "))
    dni_cread = int(input("Escriba el número de su DNI: "))
    while dni_cread < 0:
        print("El DNI no puede ser negativo, intente de nuevo")
        dni_cread = int(input("Escriba el número de su DNI: "))

    telefono_cread = int(input("Escriba su número de teléfono sin código de área: "))
    while telefono_cread < 1100000000 or telefono_cread > 1199999999:
        print("Número no válido (1100000000 a 1199999999)")
        telefono_cread = int(input("Escriba su número de teléfono sin código de área: "))    
    telefono_cread=str(telefono_cread)
    patron= "[1]{2}-[0-9]{4}-[0-9]{4}"
    numero_oculto="11-XXXX-XXXX"
    telefono_organizado=re.sub(patron,numero_oculto,telefono_cread)


    email = input("Escriba su email: ")
    coincidencias = re.findall("@", email)       
    if coincidencias==None:
        print("Email inválido, debe ser @gmail.com, @hotmail.com o @yahoo.com")
        email = input("Escriba su email: ")

    activo = True
    contraseña = input("Escriba la contraseña que desea: ")

    print("Usuario creado con éxito con la siguiente información:")
    print("\n" + "-" * 50)
    print(f"  - ID usuario : {num_usuario}")
    print(f"  - Nombre     : {nombre}")
    print(f"  - DNI        : {dni_cread}")
    print(f"  - Teléfono   : {telefono_organizado}")
    print(f"  - Email      : {email}")
    print("-" * 50 + "\n")

    datos_de_ingreso_dni.append(dni_cread)
    datos_globales_contraseñas.append(contraseña)
    datos_globales_usuarios.append([num_usuario, nombre, dni_cread, telefono_cread, email, activo])

    print("Usuario registrado con éxito")
    print("")
"""testeo de las variables"""
#region testeo
"""

registrar()
login()

"""