"""
Autor(es): Sergio Andrés Rincón Serna
Fecha: 28/05/2025
Descripcion: Este algoritmo captura credenciales y las valida
"""

from cosasestas import validate_name, validate_password, clear

control = 0 
user_list = []

while control != 3:
    print(
        """
        Bienvenido
        Registrar usuario: 1
        Ingresar: 2
        Salir: 3
        """)
    control = int(input("Seleccione una opcion: ")) #La variable control permite el funcionamiento del menú
    clear()
    
    if control == 1: 
        #Captura los datos validados con el diccionario
        data_user = {"name":"", "password":""}
        validate_user = False

        #valida y almacena el nombre de usuario
        user = False
        while (user == False):
            user_name = input("Ingrese un nombre de usuario: ")
            user = validate_name(user_name)
            print("Nombre guardado")

        #valida y almacena la contraseña
        password = False
        while (password == False):
            user_password = input("Ingrese una contraseña(No menos de 8 caracteres): ")
            password = validate_password(user_password)
            print("usuario guardado")
        
        #crea el diccionario de registros
        data_user["name"] = user_name
        data_user["password"] = user_password

        #almacena el diccionario de registros en la lista de usuarios
        user_list.append(data_user)

    elif control == 2:
        counter = 1
        while counter <= 3:
            target_password = input("Ingrese la contraseña del usuario: ")
            encontrado = False  # Bandera para saber si se encontró el usuario
            
            for user_dict in user_list:
                if user_dict['password'] == target_password:
                    print("Nombre")
                    print(f"{user_dict['name']}")
                    encontrado = True
                    counter = 4  # Salir del while
                    break  # Salir del for
                
            if not encontrado:  # Si no se encontró el usuario
                if counter == 3:
                    print("Contraseña incorrecta. Intentos agotados.")
                    break
                else:
                    print(f"Contraseña incorrecta. Intentos restantes: {3 - counter}")
                    counter += 1
                        
    elif control == 3:
        print("Hasta luego!")
    else:
        print("Ingrse una opcion valida")