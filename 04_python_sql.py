import psycopg2
import os # Importamos la librería del sistema operativo
from dotenv import load_dotenv # Importamos la función de la nueva librería

# Cargamos las variables del archivo .env en el entorno
load_dotenv()

## ---Configuración de la conexión ---
# Leemos las variables del entorno usando os.environ.get()
DB_NAME = "mi_coleccion_db"
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = "localhost"
DB_PORT = "5432"

# Variable para guardar la conexión y el cursor ¿qué es cursor?
conn = None # ¿Por qué se pone "None" y no de pone cero o deja en blanco?
cur = None


try:
    # ¿Por qué se usa "try"? ¿Para qué sirve, en qué ocasiones se usa? Dame ejemplos
    # Conectar a la base de datos
    #¿Cómo puedo saber que para conectarme debo usar ".connect" y que esa es la estructura? Me puedes explicar los puntos más relevantes de la librería psycopg2
    conn = psycopg2.connect(
        dbname = DB_NAME,
        user = DB_USER,
        password = DB_PASS,
        host = DB_HOST,
        port = DB_PORT
    )

    print("¡Conexión a la base de datos exitosa")

    #---Crear un cursor---
    # Usamos un cursor para ejecutar comandos SQL. Es como nuestro "control remoto".
    cur = conn.cursor()

    # ---Ejecutar una consulta (Leer datos)---
    print("\n--- Libros en la colección ---")
    cur.execute("SELECT id, titulo, autor, anio_publicacion FROM libros ORDER BY id;")

    # ---Recuperar y mostrar los resultados---
    # cur.fetchall() recupera todas las filas del resultado de la consulta
    libros = cur.fetchall()

    for libro in libros: #si antes no he utilizado la palabra o variable "libro" ¿de dónde sale? ¿no la tengo que definir antes? ¿Qué es una tupla? ¿Cuál es la difencia con una listas?
        # Cada 'libro' es una tupla, ej: (1, 'Cien años de soledad', 'Gabo', 1967)
        # Accedemos a los elementos por su índice: libro[0] es el id, libro[1] el título, etc.
        print(f"ID: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, Año: {libro[3]}")

except Exception as e:
    #Si ocurre cualquier error durante la conexión o consulta
    #¿Qué hace Exception? ¿Cómo y en qué casos se utiliza?
    print(f"Ocurrión un error: {e}")

finally:
    #¿Qué es finaylly?
    #Este bloque se ejecuta siempre, haya o no haya error.
    #Es una buena practica cerrar siempre el cursor y la conexión.
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
    
    print("\nLa conexión a la base de datos ha sido cerrada")