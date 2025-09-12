from database import connect_to_database
import mysql.connector

while True:
    print("\n--- 1. Crear Producto ---")
    print("\n--- 2. Ver Producto ---")
    print("\n--- 3. Actualizar Producto ---")
    print("\n--- 4. Eliminar Producto ---")
    print("\n--- 0. Salir ----")
    try:
        user_response = int(input("Seleccione una opcion: "))
        if user_response not in (0, 1, 2, 3, 4):
            raise ValueError("Error. Opcion no valida. Intente de nuevo.")
        elif user_response == 0:        
            print("Saliendo...")
            exit()
        else: 
            break
    except ValueError as err:
        print(err)    
if user_response == 1:
    try:        
        id_product = int(input("Ingrese o Escanee el ID del Producto: "))
        if id_product <= 0:
            raise ValueError("ID no válido. Intente de nuevo.")

        db_connection = connect_to_database()
        if db_connection:
            cursor = db_connection.cursor()
            try:
                cursor.execute("SELECT id_product FROM product")
                ids = [row[0] for row in cursor.fetchall()] # type: ignore

                if id_product in ids:
                    print("Error. El ID ya existe. Intente con otro ID.")
                else:
                    name_product = input("Ingrese el nombre del Producto: ").upper()
                    print("Categorias:")
                    print("1. Bebidas.")
                    print("2. Refrescos.")
                    print("3. Cerveza.")
                    print("4. Galletas.")
                    print("5. Papas.")
                    print("6. Dulces.")

                    try:
                        categoria = int(input("Seleccione una categoria (0 para cancelar): "))
                        if categoria == 0:
                            print("Cancelado, regresando al inicio...")
                            continue # type: ignore
                        if categoria not in [1, 2, 3, 4, 5, 6]:
                            raise ValueError("Categoría no válida.")

                        while True:
                            try:
                                price_product = float(input("Ingrese el precio de Compra del Producto: $"))
                                venta_product = float(input("Ingrese el precio de Venta del Producto: $"))
                                break
                            except ValueError as err:
                                print(f"Error. Dato no válido. {err}. Intente de nuevo.")

                        print(f"\n Producto listo para insertar: {id_product}, {name_product}, Cat:{categoria}, Compra:${price_product}, Venta:${venta_product}")
                        if db_connection:
                            cursor = db_connection.cursor()
                            values = (id_product, name_product, categoria, price_product, venta_product)
                            cursor.callproc("InsertProduct", values)
                            db_connection.commit()
                            cursor.execute("SELECT LAST_INSERT_ID()")
                            last_id = cursor.fetchone()[0] # type: ignore
                            print(f"Producto creado exitosamente! ID:{last_id}\n")
                            cursor.close()
                            db_connection.close()
                    except ValueError as err:
                        print(f"Error. {err}")

            except mysql.connector.Error as err:
                print(f"Error al buscar el ID del Producto: {err}")
            finally:
                cursor.close()
                db_connection.close()
    except ValueError as err:
        print(f"Error. ID no válido. {err}")
elif user_response == 2:
    while True:
        try:
            userResponse_id = int(input("Ingrese el ID del Producto a buscar (0 para cancelar): "))
            if userResponse_id == 0:
                print("Cancelado, regresando al inicio...")
                break
            if userResponse_id <= 0:
                raise ValueError("ID no válido. Intente de nuevo.") 
            else:
                db_connection = connect_to_database()
                if db_connection:
                    cursor = db_connection.cursor()
                    try:
                        cursor.execute("SELECT id_product FROM product")
                        ids = [row[0] for row in cursor.fetchall()] # type: ignore
                        if userResponse_id in ids:
                            cursor.execute("SELECT * FROM product WHERE id_product = %s", (userResponse_id,))
                            product = cursor.fetchone()
                            if product:
                                print("\n--- Detalles del Producto ---")
                                print(f"ID: {product[0]}")# type: ignore
                                print(f"Nombre: {product[1]}")# type: ignore
                                print(f"Categoria: {product[2]}")# type: ignore
                                print(f"Precio de Compra: ${product[3]}")# type: ignore
                                print(f"Precio de Venta: ${product[4]}\n")# type: ignore
                            else:
                                print("Producto no encontrado.")
                            cursor.close()
                            db_connection.close()
                            break
                        else:
                            print("Error. El ID no existe. Intente de nuevo.")
                    except mysql.connector.Error as err:
                        print(f"Error al buscar el Producto: {err}")
        except ValueError as err:
            print(f"Error. ID no válido. {err}")
elif user_response == 3:
    pass
elif user_response == 4:
    pass