# Programa de gestión de inventario

# Inventario inicial con formato {producto: (precio, cantidad)}
inventario = {
    "manzanas": (0.5, 10),
    "naranjas": (0.6, 5),
    "plátanos": (0.3, 2)
}

# Función para mostrar el inventario completo
def mostrar_inventario():
    print("\nInventario actual:")
    for producto, (precio, cantidad) in inventario.items():
        print(f"Producto: {producto}, Precio: {precio}€, Cantidad: {cantidad}")
    print()

# Función para agregar un producto al inventario
def agregar_producto():
    producto = input("Ingresa el nombre del producto: ").lower()
    precio = float(input("Ingresa el precio del producto: "))
    cantidad = int(input("Ingresa la cantidad del producto: "))
    
    if producto in inventario:
        print(f"El producto {producto} ya existe. Se actualizará la cantidad.")
        precio_actual, cantidad_actual = inventario[producto]
        inventario[producto] = (precio_actual, cantidad_actual + cantidad)
    else:
        inventario[producto] = (precio, cantidad)
    
    print(f"Producto {producto} agregado o actualizado correctamente.\n")

# Función para eliminar un producto del inventario
def eliminar_producto():
    producto = input("Ingresa el nombre del producto que deseas eliminar: ").lower()
    
    if producto in inventario:
        del inventario[producto]
        print(f"Producto {producto} eliminado correctamente.\n")
    else:
        print(f"El producto {producto} no existe en el inventario.\n")

# Función para mostrar productos con cantidades bajas
def mostrar_productos_bajos(limite_bajo=5):
    print(f"\nProductos con cantidad menor o igual a {limite_bajo}:")
    for producto, (precio, cantidad) in inventario.items():
        if cantidad <= limite_bajo:
            print(f"Producto: {producto}, Cantidad: {cantidad}")
    print()

# Menú principal del programa
def menu():
    while True:
        print("1. Mostrar inventario")
        print("2. Agregar producto")
        print("3. Eliminar producto")
        print("4. Mostrar productos con cantidades bajas")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            mostrar_inventario()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            mostrar_productos_bajos()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")

# Ejecutar el menú principal
menu()
