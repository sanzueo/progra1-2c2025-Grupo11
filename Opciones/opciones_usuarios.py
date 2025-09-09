from entidades import *
from nombres_teatroV2 import *

def _ver_usuarios():
    ver_m3(matriz3)

def _editar_usuario():
    eleccion = int(input("Seleccione el id de usuario a editar: "))
    encontrado = False
    for i in datos_globales_usuarios:
        if i[0] == eleccion:
            encontrado = True
            i[1] = input("Ingrese nombre: ")
            i[2] = int(input("Ingrese dni: "))
            i[3] = int(input("Ingrese telefono: "))
            i[4] = input("Ingrese el correo: ")
            print("Usuario editado.")
            break
    if not encontrado:
        print("No coincide con ningún id.")

def _borrar_usuario():
    eleccion = int(input("Seleccione id a eliminar: "))
    desactivado = False
    for i in datos_globales_usuarios:
        if i[0] == eleccion:
            i[5] = False
            desactivado = True

    for i in datos_globales_reserva[:]:
        if i[1] == eleccion:
            datos_globales_reserva.remove(i)

    if desactivado:
        print("Usuario borrado (desactivado).")
    else:
        print("No coincide con ningún id.")

def menu_usuarios(admin: bool):
    # Un solo ciclo por llamada, como tu código original
    if admin == False:
        print("\n1-Ver usuario\n2-¿¿¿¿Editar usuario????")
        usuario_i = int(input("Elige una opcion: "))

        if usuario_i == 1:
            _ver_usuarios()
        elif usuario_i == 2:
            _editar_usuario()
        else:
            print("Opción inválida.")

    else:
        print("\n1-Ver usuario\n2-Editar usuario\n3-Borrar usuario")
        usuario_i = int(input("Elige una opcion: "))

        if usuario_i == 1:
            _ver_usuarios()
        elif usuario_i == 2:
            _editar_usuario()
        elif usuario_i == 3:
            _borrar_usuario()
        else:
            print("Opción inválida.")
