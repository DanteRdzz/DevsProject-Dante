import pandas as pd
import _mysql_connector
import openpyxl
import hashlib
from database import connect_to_database

def insert_user(name, apellido, email, hashed_password):
    db_connection = connect_to_database()
    if db_connection:
        cursor = db_connection.cursor()
        values = (name, apellido, email, hashed_password)
        try:
            cursor.callproc("InsertUser", values)
            db_connection.commit()
            cursor.execute("SELECT LAST_INSERT_ID()")
            user_id = cursor.fetchone()[0] # type: ignore
            print(f"Cuenta creada exitosamente! ID: {user_id}")
        except _mysql_connector.Error as err:
            print(f"Error al crear la cuenta: {err}")
def verify_user(email, password):
    db_connection = connect_to_database()
    if db_connection:
        cursor = db_connection.cursor()
        try:
            query = ("SELECT id_user, name_user, lastName_user, email_user, password_user FROM users WHERE email_user = %s")
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            id_0 = result[0] # type: ignore
            name_0 = result[1] # type: ignore
            lastName_0 = result[2] # type: ignore 
            email_0 = result[3] # type: ignore
            password_0 = result[4] # type: ignore
            if email == email_0 and password == password_0:
                if id_0 == 1:
                    print(f"Bienvenido Admin {name_0} {lastName_0}")
                else:
                    print(f"Bienvenido {name_0} {lastName_0}")
            else:
                print("Error. Usuario o contraseña son incorrectos")
                
        except _mysql_connector.Error as err:
            print(f"Error al buscar la cuenta {err}")
while True:
    print("BIENVENIDO")
    print("1. INICIAR SESION")
    print("2. REGISTRARSE")
    print("3. SALIR")
    while True:
        try:
            opcion_login = int(input("Seleccione una opcion del menu: "))
            if opcion_login not in [1, 2]:
                raise ValueError("Opcion no valida")
            else:
                break
        except ValueError as ve:
            print(ve)
    if opcion_login == 1:
        email_verify = input("Ingresa tu correo: ")
        password_verify = input("Ingresa tu contraseña: ")
        hashed_password_verify = hashlib.sha256(password_verify.encode()).hexdigest()
        verify_user(email_verify, hashed_password_verify)
    elif opcion_login == 2:
        name = input("Ingresa su nombre: ").upper()
        apellido = input("Ingrese su apellido: ").upper()
        email = input("Ingrese su correo electronico: ")
        password = input("Ingrese su contraseña: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest() # Contraseña a guardar en la db
        insert_user(name, apellido, email, hashed_password)
    elif opcion_login == 3:
        break