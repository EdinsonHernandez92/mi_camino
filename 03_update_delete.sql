SELECT *
FROM libros;

UPDATE libros
SET anio_publicacion = 1983
WHERE titulo = 'La casa de los espíritus';

DELETE
FROM libros
WHERE id = 2;