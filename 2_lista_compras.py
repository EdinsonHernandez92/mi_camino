# Este proyecto nos introducirá a dos conceptos increíblemente importantes: listas y bucles.
"""
Conceptos Nuevos:
Listas: En Python, una lista es una colección de elementos guardados en una sola variable.
Es como tener una caja donde puedes meter varias cosas. Se definen con corchetes [].
"""

## Una lista vacía
#mi_lista_vacia = []

## Una lista con elementos
#frutas = ["manzana", "banano", "naranja"]
#print(frutas)

"""
Bucles while: Un bucle while repite un bloque de código una y otra vez mientras una condición sea verdadera.
Lo usaremos para que nuestro programa se siga ejecutando y nos permita añadir varios artículos sin tener que reiniciarlo cada vez.
"""

# 1. Creamos una lista vacía para guardar nuestros artículos de compra.
lista_de_compras = []

print("--- ¡Bienvenido a tu Lista de Compras! ---")

# 2. Iniciamos un bucle infinito que solo se detendrá cuando el usuario lo decida.
while True:
    
    # 3. Pedimos al usuario que elija una acción.
    opcion = input("Escribe AÑADIR para agregar un artículo, VER para mostrar la lista, o SALIR para terminar: ")
    
    # Hacemos la opción ingresada mayúscula para que no importe si escriben "salir", "Salir" o "SALIR".
    opcion = opcion.upper()
    
    # 4. Verificamos si el usuario quiere salir.
    if opcion == "SALIR":
        print("¡Gracias por usar la lista de compras! Adiós.")
        break # La instrucción 'break' rompe el bucle y termina el programa.

    if opcion == "AÑADIR":
        nuevo_articulo = input("Escribe el artículo a añadir: ")
        lista_de_compras.append(nuevo_articulo)
    
    elif opcion == "VER":
        print(lista_de_compras)

"""
Un Pequeño Consejo para Mejorar (Buenas Prácticas)
Tu código funciona, pero te daré un pequeño consejo de estilo y eficiencia que te servirá mucho en el futuro.
Cuando tienes una serie de condiciones que se excluyen mutuamente (como AÑADIR, VER, SALIR), es una buena práctica encadenarlas con if, elif, y else.
Python evalúa estas condiciones en orden y, en cuanto encuentra una que es verdadera, ejecuta su bloque y ya no revisa las demás.
Aquí, si el usuario escribe "AÑADIR", Python primero comprueba if opcion == "SALIR" (falso), luego comprueba if opcion == "AÑADIR" (verdadero, y ejecuta el código),
y después, innecesariamente, comprueba elif opcion == "VER" (falso).

Una versión ligeramente más eficiente y clara sería:
if opcion == "SALIR":
    # ...
elif opcion == "AÑADIR":
    # ...
elif opcion == "VER":
    # ...

De esta forma, en cuanto una opción es verdadera, las demás se ignoran.
Es un detalle menor en este programa, pero una excelente costumbre para programas más grandes.    

Un Extra Opcional: Mostrando la Lista de Forma Elegante
Viste que print(lista_de_compras) funciona, pero muestra la lista con corchetes y comillas. Si quieres mostrarla como una lista real,
puedes usar otro tipo de bucle, el bucle for, que está diseñado para recorrer elementos de una colección.

Podrías reemplazar tu bloque "VER" con esto:
elif opcion == "VER":
    print("\n--- Tu Lista de Compras ---")
    # Este bucle 'for' recorre cada 'articulo' en la 'lista_de_compras'
    for articulo in lista_de_compras:
        # Imprime cada artículo en su propia línea
        print(f"- {articulo}")
    print("---------------------------\n")

"""