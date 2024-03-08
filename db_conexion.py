# db_conexion.py
import mysql.connector
from mysql.connector import Error

#funcion para generar la conexion a la base de datos de maria db
def conexion_base_de_datos():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',      # Usuario de la base de datos (en este caso, root)
            password='bcb96dbdb1',     # Contraseña vacía porque no se ha establecido una contraseña para root
            database='sistema_inventario'  # Nombre de tu base de datos
        )
        if conexion.is_connected():
            print("Conexión establecida con éxito.")
            return conexion
    except mysql.connector.Error as error:
        print(f"Error al conectar a la base de datos: {error}")
        return None

def ejecutar_consulta(conexion, consulta):
    try:
        cursor = conexion.cursor()
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as error:
        print(f"Error al ejecutar la consulta: {error}")
        return None

if __name__ == "__main__":
    conexion = conexion_base_de_datos()
    if conexion:
        # Realizamos una consulta
        
        consulta = "SELECT * FROM Administrador;" 
        resultados = ejecutar_consulta(conexion, consulta)
        if resultados:
            print("Resultados de la consulta:")
            for fila in resultados:
                print(fila)
        conexion.close()