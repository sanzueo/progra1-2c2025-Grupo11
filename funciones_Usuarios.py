from nombres_teatroV2 import datos_globales_usuarios, dni_en_uso, datos_globales_reserva,id_usuarios
from entidades.Usuarios import ver_m3,id_usuarios,ver_busqueda_usuarios
from funciones_Reservas import obt_id_Actual
import re

def vista_Usuarios(admin):
        if admin: 
            eleccion = int(input("\033[96m1-VER TODOS LOS USUARIOS\n2-BUSCAR USUARIO POR ID:\033[0m"))
            if eleccion == 1:
                ver_m3(datos_globales_usuarios) 
            elif eleccion == 2:

                eleccion = int(input("Ingrese ID a buscar: "))

                matriz_enct = []

                encontrado = False

                for i in datos_globales_usuarios:
                    if i[0] == eleccion:
                        encontrado = True
                        matriz_enct.append(i)

                if not encontrado:
                    print("ID no encontrado.")
                else:
                    ver_busqueda_usuarios(matriz_enct)
        elif admin == False:
            id = obt_id_Actual()

            mat_act = []

            for i in datos_globales_usuarios:
                if id == i[0]:
                    mat_act.append(i)

            ver_busqueda_usuarios(mat_act)

def edicion_usuario(admin):
    if admin:
        while True:
            try:
                eleccion = int(input("Seleccione el id de usuario a editar: "))
                break
            except (ValueError,KeyboardInterrupt):
                print("ponga caracteres validos")
                continue
        if eleccion not in id_usuarios:
            print("ID no encontrad0.")
        else:
            for i in datos_globales_usuarios:
                if i[0] == eleccion:
                    while True:
                        try:
                            opcion = int(input(
                            "\n\033[92m=== MENU DE EDICIÓN ===\033[0m\n"
                            "\033[35m  → [0] Editar nombre\033[0m\n"
                            "\033[35m  → [1] Editar DNI \033[0m\n"
                            "\033[35m  → [2] Editar telefono\033[0m\n"
                            "\033[35m  → [3] Editar correo\033[0m\n"
                            "\033[35m  → [4] Editar estado a Inactivo\033[0m\n"
                            "\033[35m  → [5] Editar estado a activo\033[0m\n"
                            "\033[1;35m Seleccione una opción: \033[0m"
                            ))
                            if opcion in (0,1,2,3,4,5):
                                break
                        except(KeyboardInterrupt,ValueError):
                            print("ponga caracteres validos")
                            continue
                    
                    if opcion == 0:
                        i[1] = input("\033[36m Ingrese nombre a cambiar: \033[0m")
                    elif opcion == 1:
                        while True:
                            try:
                                dni = int(input("\033[36m Escriba el dni por el que desea cambiar: \033[0m"))
                                if dni > 0:
                                    i[2]=dni
                                    break
                                else:
                                    print("\033[91m El DNI no puede ser negativo, intente de nuevo.\033[0m")
                            except ValueError:
                                print("no se admite otra cosa que no sean enteros")
                        
                    elif opcion == 2:
                        while True:
                            try:
                                telefono = int(input("\033[36mIngrese el numero de telefono por el que desea cambiar: \033[0m"))
                                if telefono > 1100000000 and telefono < 1199999999:
                                    i[3]=telefono
                                    break
                                else:
                                    print("\033[91mEl número debe estar entre 1100000000 y 1199999999.\033[0m")
                            except ValueError:
                                print("\033[91mError: solo se admiten números.\033[0m")
                    elif opcion == 3:
                        while True:
                            try:
                                #el usuario escribe su email 
                                email = input("\033[36m Escriba su nuevo email: \033[0m")
                                
                                #validaciones basicas de email
                                arroba = re.findall('@', email)
                                punto  = re.findall(r'\.', email)   

                                if len(arroba) !=0 and len(punto) != 0:
                                    i[4]=email
                                    break
                                else: 
                                    print("\033[91m Email inválido, debe contener '@' y '.' \033[0m")
                            except(KeyboardInterrupt, ValueError):
                                print("ponga caracteres validos")
                                continue

                    elif opcion == 4:
                        i[5]= False
                    elif opcion == 5:
                        i[5] = True
    

    elif admin==False:  # EDITAR USUARIO
        for i in datos_globales_usuarios:
            if i[2] == dni_en_uso[0]:
                print("\033[96mSe ha accedido a su perfil\033[0m")
                while True:
                    try:
                        opcion = int(input(
                            "\n\033[92m=== MENÚ DE EDICIÓN ===\033[0m\n"
                            "\033[35m  → [0] Editar nombre\033[0m\n"
                            "\033[35m  → [1] Editar teléfono\033[0m\n"
                            "\033[35m  → [2] Editar correo\033[0m\n"
                            "\033[1;35mSeleccione una opción: \033[0m"
                        ))

                        if opcion in (0,1,2):
                            break
                    except(ValueError,KeyboardInterrupt):
                            print("ponga caracteres validos")
                            continue
                if opcion == 0:
                    i[1] = input("\033[36mIngrese nombre: \033[0m")

                elif opcion == 1:
                    while True:
                        try:
                            telefono = int(input("\033[36mIngrese el numero de telefono por el que desea cambiar: \033[0m"))
                            if telefono > 1100000000 or telefono < 1199999999:
                                i[3]=telefono
                                break
                            else:
                                print("\033[91mEl número debe estar entre 1100000000 y 1199999999.\033[0m")
                        except ValueError:
                            print("\033[91mError solo se admiten números.\033[0m")

                elif opcion == 2:
                    #el usuario escribe su email 
                    email = input("\033[36m Escriba su nuevo email: \033[0m")
                    
                    #validaciones basicas de email
                    arroba = re.findall('@', email)
                    punto  = re.findall(r'\.', email)   

                    if len(arroba) ==0 and len(punto) == 0:
                        print("\033[91m Email inválido, debe contener '@' y '.' \033[0m")
                        email = input("\033[36m Escriba su email: \033[0m")
                    else:
                        i[4]=email
    
                print("\033[92mSe ha editado el usuario exitosamente.\033[0m")

def borrado_usuarios():
        while True:
            try:
                eleccion = int(input("Seleccione id a eliminar: "))
                while eleccion not in id_usuarios:
                    print("ID no encontrado")
                else:
                    break
            except(ValueError,KeyboardInterrupt):
                print("porfavor ponga caracteres valido")
                continue
            
        print("\033[1;91m Recuerde que esta acción es irrevertible \033[0m")
        print()
        print("\033[1;91m Por favor vuelva a dar confirmación \033[0m")
        
        while True:
            try:
                opcion = int(input(
                    "\033[35m  → [1] Eliminar cuenta\033[0m\n"
                    "\033[35m  → [2] Volver al menú\033[0m\n"
                ))
                if opcion in (1,2):
                    break
                else:
                    print("solo 1 y 2 son numeros validos")
            except(KeyboardInterrupt,ValueError):
                print("porfavor ponga caracteres valido")
                continue

        if opcion == 1:
            for i in datos_globales_usuarios:
                if i[0] == eleccion:
                    i[5] = False   
            for i in datos_globales_reserva[:]:
                if i[1] == eleccion:
                    datos_globales_reserva.remove(i)
            print(f"Usuario con ID {eleccion} y las reservas que tiene asociadas fueron eliminados correctamente.")
        elif opcion == 2:
                print("volviendo al menu")