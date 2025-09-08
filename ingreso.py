from nombres_teatroV2 import *
from funciones_de_teatroV2 import *
import re

def imprimir_ingreso():
    ingreso = int(input(
    "\n=== MENÚ DE INGRESO ===\n"
    "0 - Ingresar con un usuario existente\n"
    "1 - Crear un usuario nuevo\n"
    "Seleccione una opción: "
    ))
    return ingreso

def banner():
    print("=" * 50)
    print(" " * 15 + " SISTEMA DE LOGIN ")
    print("=" * 50)

def menu_login():
    banner()
    print("\n")
    print(" " * 10 + "1) Iniciar Sesión")
    print(" " * 10 + "2) Registrarse")
    print(" " * 10 + "3) Recuperar Contraseña")
    print(" " * 10 + "0) Salir")
    print("\n" + "=" * 50)

    opcion = input("👉 Elige una opción: ")
    return opcion

def login():
    dni_ingres=int(input("escriba su dni para verificacion "))
    while dni_ingres not in datos_de_ingreso_dni and dni_ingres not in dni_admins:
        print("id no encontrado revise que este bien su dni")
        dni_ingres=int(input("escriba su dni para verificacion "))


    contraseña=input("escriba su contraseña de usuario ")
        
    while not (
        (dni_ingres in datos_de_ingreso_dni and contraseña in datos_globales_contraseñas) or
        (dni_ingres in dni_admins and contraseña in contraseñas_admin)
    ):

        print("su contraseña o dni no son correctos")
        vuelta = int(input(
            "\n=== MENÚ DE INGRESO ===\n"
            "0 - volver al menu de ingreso\n"
            "1 - Ingresar nuevamente el dni\n"
            "2 - ingresar nuevamente la contraseña\n"
            "Seleccione una opción: "
        ))

        while vuelta !=0 and vuelta!=1 and vuelta!=2:
            print("ese numero no esta dentro del rango")#0 es menu 1 ese dni 2 es contraseña
            vuelta = int(input(
                "\n=== MENÚ DE INGRESO ===\n"
                "0 - volver al menu de ingreso\n"
                "1 - Ingresar nuevamente el dni\n"
                "2 - ingresar nuevamente la contraseña\n"
                "Seleccione una opción: "
            ))
        if vuelta==0:
            registrar()  #habria que ver
        elif vuelta==1:
            dni_ingres=int(input("escriba su dni para verificacion: "))
        elif vuelta==2:
            contraseña=(input("escriba su contraseña para verificacion: "))



    if contraseña in contraseñas_admin and dni_ingres in dni_admins:
        print("Ingreso conseguido como ADMIN")
        return True
    elif busqueda(dni_ingres, contraseña):
        print("Ingreso conseguido como USUARIO")
        return False


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


    print(f"se a creado su usuario con la siguiente informacion")
    print(f"-"*25)
    print(f"numero de usuario: {num_usuario}\nnombre: {nombre}\ndni: {dni_cread}\nnumero: {telefono_organizado}\nemail:{email}")
    print("-"*25)

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