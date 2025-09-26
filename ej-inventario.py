def mostrar_menu():
    print("\n=== Menú de Inventario ===")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar inventario")
    print("4. Salir")

def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ").strip().title()
    if nombre in inventario:
        print("⚠️ El producto ya existe en el inventario.")
    else:
        try:
            cantidad = int(input("Ingrese la cantidad inicial: "))
            if cantidad < 0:
                print("⚠️ La cantidad no puede ser negativa.")
            else:
                inventario[nombre] = cantidad
                print(f"✅ Producto '{nombre}' agregado con cantidad {cantidad}.")
        except ValueError:
            print("⚠️ La cantidad debe ser un número entero.")

def eliminar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip().title()
    if nombre in inventario:
        del inventario[nombre]
        print(f"🗑️ Producto '{nombre}' eliminado.")
    else:
        print("⚠️ El producto no existe en el inventario.")

def mostrar_inventario(inventario):
    if not inventario:
        print("📦 El inventario está vacío.")
    else:
        print("\n=== Inventario Actual ===")
        for nombre, cantidad in inventario.items():
            print(f"- {nombre}: {cantidad}")

def main():
    inventario = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            eliminar_producto(inventario)
        elif opcion == "3":
            mostrar_inventario(inventario)
        elif opcion == "4":
            print("👋 Saliendo del programa...")
            break
        else:
            print("⚠️ Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
