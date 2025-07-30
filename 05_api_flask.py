# Importaciones necesarias
import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, jsonify, request

# Cargar las variables de entorno
load_dotenv()

# Configuración de la conexión a la BD
DB_NAME = "mi_coleccion_db"
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = "localhost"
DB_PORT = "5432"

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# --- Función para conectar a la BD ---
# Creamos una función para no repetir el código de conexión
def get_db_connection():
    conn = psycopg2.connect(
        dbname = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT
    )
    return conn

# --- Endpoints (Rutas o "Puertas" de la API) ---

@app.route('/')
def hola_mundo():
    return '¡Bienvenido a mi API de Libros!'

@app.route('/libros', methods=['GET', 'POST'])
def manejar_libros():
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        #Si el método es POST, creamos un nuevo libro
        if request.method == 'POST':
            datos_libro = request.get_json()
            titulo = datos_libro['titulo']
            autor = datos_libro['autor']
            anio_publicacion = datos_libro['anio_publicacion']
        
            cur.execute(
                "INSERT INTO libros (titulo, autor, anio_publicacion) VALUES (%s, %s, %s);",
                (titulo, autor, anio_publicacion)
            )
            conn.commit()

            return jsonify({"mensaje": "Libro añadido con éxito"}), 201
    
        #Si el método es GET, devolvemos todos los libros
        elif request.method == 'GET':
            cur.execute("SELECT * FROM libros ORDER BY id;")
            rows = cur.fetchall()
            libros=[]
            for row in rows:
                libros.append({
                    "id": row[0],
                    "titulo": row[1],
                    "autor": row[2],
                    "anio_publicacion": row[3]
                })
            return jsonify(libros)
    except Exception as e:
        return jsonify({"error":str(e)}), 500
    finally:
        if conn:
            conn.close()

@app.route('/libros/<int:libro_id>', methods=['GET', 'PUT', 'DELETE'])
def manejar_libro_especifico(libro_id):
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        #---OBTENER UN LIBRO (GET)---
        if request.method == 'GET':
            cur.execute("SELECT * FROM libros WHERE id = %s;", (libro_id,))
            row = cur.fetchone()
            if row:
                libro_encontrado = {
                    "id": row[0], "titulo": row[1], "autor": row[2], "anio_publicacion": row[3]
                }
                return jsonify(libro_encontrado)
            return jsonify({"mensaje": "Libro no encontrado"}), 404
        
        #---ACTUALIZAR UN LIBRO (PUT)---
        elif request.method == 'PUT':
            datos_nuevos = request.get_json()
            titulo = datos_nuevos['titulo']
            autor = datos_nuevos['autor']
            anio_publicacion = datos_nuevos['anio_publicacion']

            cur.execute(
                "UPDATE libros SET titulo = %s, autor = %s, anio_publicacion =%s WHERE id = %s;",
                (titulo, autor, anio_publicacion, libro_id)
            )
            conn.commit()
            return jsonify({"mensaje": "Libro actualizado con éxito"})
        #---ELIMINAR UN LIBRO (DELETE)---
        elif request.method == 'DELETE':
            cur.execute("DELETE FROM libros WHERE id = %s;", (libro_id,))
            conn.commit()
            return jsonify({"mensaje": "Libro eliminado con éxito"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

# --- Iniciar la aplicación ---
if __name__ == '__main__':
    app.run(debug=True)