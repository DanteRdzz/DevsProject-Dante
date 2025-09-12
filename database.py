import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Cambia este usuario si es necesario
            password="GearsofWar_3",  # Cambia la contraseña
            database="metodologias"
        )
        if connection.is_connected():
            return connection
    except Exception as e:
        print(f"Error al conectar: {e}")
        return None
    
