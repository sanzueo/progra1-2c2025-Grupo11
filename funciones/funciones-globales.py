usuarios = [
    {
        "id": 1,
        "nombre": "Juan Perez",
        "dni": 12345678,
        "telefono": "123-456-7890",
        "correo": "juanperez@outlook.com",
        "estado": True
    },
    {
        "id": 2,
        "nombre": "María López",
        "dni": 23456789,
        "telefono": "234-567-8901",
        "correo": "marialopez@gmail.com",
        "estado": True
    },
    {
        "id": 3,
        "nombre": "Carlos García",
        "dni": 34567890,
        "telefono": "345-678-9012",
        "correo": "cgarcia@yahoo.com",
        "estado": False
    },
    {
        "id": 4,
        "nombre": "Ana Fernández",
        "dni": 45678901,
        "telefono": "456-789-0123",
        "correo": "ana.fernandez@mail.com",
        "estado": True
    },
    {
        "id": 5,
        "nombre": "Luis Martínez",
        "dni": 56789012,
        "telefono": "567-890-1234",
        "correo": "luis.martinez@empresa.com",
        "estado": True
    },
    {
        "id": 6,
        "nombre": "Sofía González",
        "dni": 67890123,
        "telefono": "678-901-2345",
        "correo": "sofia.gonzalez@correo.com",
        "estado": False
    },
    {
        "id": 7,
        "nombre": "Mateo Ramírez",
        "dni": 78901234,
        "telefono": "789-012-3456",
        "correo": "mateo.ramirez@dominio.com",
        "estado": True
    },
    {
        "id": 8,
        "nombre": "Valentina Torres",
        "dni": 89012345,
        "telefono": "890-123-4567",
        "correo": "valentina.torres@hotmail.com",
        "estado": True
    },
    {
        "id": 9,
        "nombre": "Nicolás Herrera",
        "dni": 90123456,
        "telefono": "901-234-5678",
        "correo": "nicolas.herrera@mail.net",
        "estado": False
    },
    {
        "id": 10,
        "nombre": "Camila Díaz",
        "dni": 11223344,
        "telefono": "012-345-6789",
        "correo": "camila.diaz@service.org",
        "estado": True
    }
]

reservas = [
    # id_reserva, id_usuario, sector, id_show, precio
    [1, 1, "vip", 1000, 150000],
    [2, 2, "platea", 1001, 120000],
    [3, 3, "campo", 1002, 80000],
    [4, 4, "vip", 1001, 150000],
    [5, 5, "vip", 1003, 110000],
    [6, 2, "campo", 1004, 75000],
    [7, 6, "platea", 1005, 200000],
    [8, 7, "platea", 1002, 115000],
    [9, 8, "campo", 1006, 70000],
    [10, 9, "vip", 1007, 180000],
    [11, 10, "platea", 1000, 125000]
]

def mostrar_tabla(dato, opcion):

    #matriz
    if opcion == 1:

        #Encabezado de la tabla
        print(f"\033[32m{'-'*73}\033[0m")
        print(f"\033[32m{'IDs':<8}  {'ID Usuario':<13}\033  \033[35m{'Ubicación':>10}  {'ID Show':>12}\033[0m  \033[34m{'Precio':>14}\033[0m")
        print(f"\033[32m{'-'*73}\033[0m")

        for fila in dato:
            print(f"\033[32m{fila[0]:<8}  {fila[1]:<13}\033[35m  {fila[2]:>10}  {fila[3]:>10}\033[0m  \033[34m{fila[4]:>14}\033[0m")
    
    #diccionario
    elif opcion == 2:
        #Encabezado de la tabla
        print(f"\033[32m{'-'*73}\033[0m")
        for usuario in dato:
            lista= list(usuario.keys())
        print(f"\033[32m{lista[0]:<8}  {lista[1]:<15}\033  \033[35m{lista[2]:>15}  {lista[3]:>25}\033[0m  \033[34m{lista[4]:>15} {lista[5]:>15}\033[0m")
        print(f"\033[32m{'-'*73}\033[0m")

        for fila in dato:
            for item in fila:
                if fila[item] == True:
                    print(f"\033[32m{'Activo':<25}\033[0m", end="  ")
                elif fila[item] == False:
                    print(f"\033[31m{'Inactivo':<25}\033[0m", end="  ")
                else:
                    print(f"\033[32m{fila[item]:<25}\033[0m", end="  ")
            print()


mostrar_tabla(reservas, 1)