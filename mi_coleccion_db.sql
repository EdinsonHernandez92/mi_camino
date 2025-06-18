-- Creamos una tabla llamada 'libros' para guardar nuestra colección.
CREATE TABLE libros (
	id SERIAL PRIMARY KEY,
	titulo VARCHAR(255) NOT NULL,
	autor VARCHAR(255) NOT NULL,
	anio_publicacion INTEGER
);
-- Insertamos nuestro primer libro en la tabla 'libros'.
INSERT INTO libros (titulo, autor, anio_publicacion) 
VALUES ('Cien años de soledad', 'Gabriel García Márquez', 1967);

INSERT INTO libros (titulo, autor, anio_publicacion) 
VALUES ('El amor en los tiempos del cólera', 'Gabriel García Márquez', 1985);

INSERT INTO libros (titulo, autor, anio_publicacion) 
VALUES ('La casa de los espíritus', 'Isabel Allende', 1982);

-- Seleccionamos TODAS las columnas (*) de la tabla 'libros'.
SELECT * 
FROM libros;