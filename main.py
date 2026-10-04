# Sistema de gestión básica de productos holísticos y esotéricos
# Pre-entrega del proyecto - Python Inicial
#
# Cada producto es una sublista de tres elementos: [nombre, categoría, precio]
# El precio se maneja en pesos, sin centavos (número entero).

# Lista de productos con 10 productos precargados
productos = [
    ["Incienso de sándalo", "Inciensos", 1500],
    ["Incienso de palo santo", "Inciensos", 2200],
    ["Cuarzo rosa", "Cristales", 4500],
    ["Amatista en bruto", "Cristales", 6800],
    ["Péndulo de cuarzo", "Péndulos", 7500],
    ["Vela de soja de lavanda", "Velas", 3200],
    ["Vela ritual de siete colores", "Velas", 2800],
    ["Mazo de tarot Rider-Waite", "Oráculos", 15000],
    ["Sahumerio de salvia blanca", "Sahumerios", 3900],
    ["Pulsera de ojo de tigre", "Amuletos", 5200],
]

while True:
    print("=" * 40)
    print("Sistema de gestión de productos holísticos")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Elegí una opción (1-5): ").strip()

    if opcion == "1":
        print("\n--- Agregar producto ---")

        # Validación del nombre: no puede estar vacío
        nombre = input("Nombre del producto: ").strip()
        while nombre == "":
            print("Error: el nombre no puede estar vacío.")
            nombre = input("Nombre del producto: ").strip()

        # Validación de la categoría: no puede estar vacía
        categoria = input("Categoría del producto: ").strip()
        while categoria == "":
            print("Error: la categoría no puede estar vacía.")
            categoria = input("Categoría del producto: ").strip()

        # Validación del precio: solo números enteros mayores a 0
        precio_texto = input("Precio (sin centavos): ").strip()
        while not precio_texto.isdigit() or int(precio_texto) == 0:
            print("Error: ingresá solo un número entero mayor a 0.")
            precio_texto = input("Precio (sin centavos): ").strip()
        precio = int(precio_texto)

        # Cada producto se guarda como una sublista de tres elementos
        producto = [nombre.title(), categoria.title(), precio]
        productos.append(producto)
        print(f"\nProducto '{producto[0]}' agregado correctamente.\n")

    elif opcion == "2":
        print("\n--- Lista de productos ---")

        if len(productos) == 0:
            print("Todavía no hay productos cargados.\n")
        else:
            for i in range(len(productos)):
                print(f"{i + 1}.")
                print(f"   Nombre: {productos[i][0]}")
                print(f"   Categoría: {productos[i][1]}")
                print(f"   Precio: ${productos[i][2]}")
            print()

    elif opcion == "3":
        print("\n--- Buscar producto ---")

        if len(productos) == 0:
            print("Todavía no hay productos cargados.\n")
        else:
            busqueda = input("Nombre del producto a buscar: ").strip().lower()
            while busqueda == "":
                print("Error: escribí algo para buscar.")
                busqueda = input("Nombre del producto a buscar: ").strip().lower()

            encontrados = 0
            for i in range(len(productos)):
                # Se busca el texto dentro del nombre, sin importar mayúsculas
                if busqueda in productos[i][0].lower():
                    print(f"{i + 1}.")
                    print(f"   Nombre: {productos[i][0]}")
                    print(f"   Categoría: {productos[i][1]}")
                    print(f"   Precio: ${productos[i][2]}")
                    encontrados += 1

            if encontrados == 0:
                print("No se encontraron resultados.\n")
            else:
                print(f"\nProductos encontrados: {encontrados}\n")

    elif opcion == "4":
        print("\n--- Eliminar producto ---")

        if len(productos) == 0:
            print("Todavía no hay productos cargados.\n")
        else:
            for i in range(len(productos)):
                print(f"{i + 1}. {productos[i][0]} - {productos[i][1]} - ${productos[i][2]}")

            numero_texto = input("Número del producto a eliminar: ").strip()

            # Validamos que sea un número y que esté dentro de la lista
            while not numero_texto.isdigit() or int(numero_texto) < 1 or int(numero_texto) > len(productos):
                print(f"Error: ingresá un número entre 1 y {len(productos)}.")
                numero_texto = input("Número del producto a eliminar: ").strip()

            posicion = int(numero_texto) - 1
            eliminado = productos.pop(posicion)
            print(f"\nSe eliminó el producto: {eliminado[0]}\n")

    elif opcion == "5":
        print("\n¡Gracias por usar el sistema! Namasté 🙏")
        break

    else:
        print("\nOpción no válida. Tenés que elegir un número entre 1 y 5.\n")
