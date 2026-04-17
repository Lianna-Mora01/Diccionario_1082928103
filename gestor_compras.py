"""
Gestor de lista de compras
Programa para agregar, visualizar y gestionar artículos de compra
"""

# Lista para almacenar los artículos de compra
articulos = []

def agregar_articulo():
    """
    Solicita datos al usuario y agrega un artículo a la lista
    """
    print("\n--- AGREGAR ARTÍCULO ---")
    
    # Solicitar datos al usuario
    producto = input("Nombre del producto: ").strip()
    
    if not producto:
        print("❌ El nombre del producto no puede estar vacío.")
        return
    
    try:
        precio = float(input("Precio del producto: $"))
        if precio < 0:
            print("❌ El precio no puede ser negativo.")
            return
    except ValueError:
        print("❌ Por favor ingresa un precio válido (número).")
        return
    
    try:
        cantidad = int(input("Cantidad: "))
        if cantidad <= 0:
            print("❌ La cantidad debe ser mayor a 0.")
            return
    except ValueError:
        print("❌ Por favor ingresa una cantidad válida (número entero).")
        return
    
    # Crear diccionario con el artículo
    articulo = {
        "producto": producto,
        "precio": precio,
        "cantidad": cantidad
    }
    
    # Agregar a la lista
    articulos.append(articulo)
    print(f"✅ '{producto}' agregado correctamente a la lista.")


def mostrar_articulos():
    """
    Muestra todos los artículos en la lista
    """
    print("\n--- LISTA DE COMPRAS ---")
    
    if not articulos:
        print("La lista está vacía.")
        return
    
    total_general = 0
    print(f"\n{'Nº':<3} {'Producto':<20} {'Precio':<10} {'Cantidad':<10} {'Subtotal':<10}")
    print("-" * 60)
    
    for i, articulo in enumerate(articulos, 1):
        producto = articulo["producto"]
        precio = articulo["precio"]
        cantidad = articulo["cantidad"]
        subtotal = precio * cantidad
        total_general += subtotal
        
        print(f"{i:<3} {producto:<20} ${precio:<9.2f} {cantidad:<10} ${subtotal:<9.2f}")
    
    print("-" * 60)
    print(f"{'TOTAL':<33} ${total_general:.2f}")


def eliminar_articulo():
    """
    Elimina un artículo de la lista
    """
    if not articulos:
        print("\n❌ La lista está vacía.")
        return
    
    mostrar_articulos()
    
    try:
        numero = int(input("\nIngresa el número del artículo a eliminar: "))
        if 1 <= numero <= len(articulos):
            articulo_eliminado = articulos.pop(numero - 1)
            print(f"✅ '{articulo_eliminado['producto']}' eliminado de la lista.")
        else:
            print(f"❌ Número inválido. Debe estar entre 1 y {len(articulos)}.")
    except ValueError:
        print("❌ Por favor ingresa un número válido.")


def limpiar_lista():
    """
    Limpia todos los artículos de la lista
    """
    if articulos:
        confirmar = input("\n⚠️  ¿Deseas borrar toda la lista? (s/n): ").lower()
        if confirmar == 's':
            articulos.clear()
            print("✅ Lista limpiada correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print("\n❌ La lista ya está vacía.")


def buscar_producto():
    """
    Busca un producto por nombre en la lista
    """
    if not articulos:
        print("\n❌ La lista está vacía.")
        return
    
    busqueda = input("\nIngresa el nombre del producto a buscar: ").lower().strip()
    
    # Filtrar productos que coincidan con la búsqueda
    resultados = [art for art in articulos if busqueda in art["producto"].lower()]
    
    if resultados:
        print(f"\n✅ Se encontraron {len(resultados)} resultado(s):")
        print(f"\n{'Producto':<20} {'Precio':<10} {'Cantidad':<10}")
        print("-" * 40)
        for art in resultados:
            print(f"{art['producto']:<20} ${art['precio']:<9.2f} {art['cantidad']:<10}")
    else:
        print(f"\n❌ No se encontraron productos con '{busqueda}'.")


def filtrar_por_precio():
    """
    Filtra productos por rango de precio
    """
    if not articulos:
        print("\n❌ La lista está vacía.")
        return
    
    try:
        precio_min = float(input("\nPrecio mínimo: $"))
        precio_max = float(input("Precio máximo: $"))
        
        if precio_min > precio_max:
            print("❌ El precio mínimo no puede ser mayor al máximo.")
            return
        
        # Filtrar usando diccionarios con list comprehension
        filtrados = [art for art in articulos 
                    if precio_min <= art["precio"] <= precio_max]
        
        if filtrados:
            print(f"\n✅ Se encontraron {len(filtrados)} artículos en el rango ${precio_min:.2f} - ${precio_max:.2f}")
            print(f"\n{'Producto':<20} {'Precio':<10} {'Cantidad':<10}")
            print("-" * 40)
            for art in filtrados:
                print(f"{art['producto']:<20} ${art['precio']:<9.2f} {art['cantidad']:<10}")
        else:
            print(f"\n❌ No hay productos en el rango ${precio_min:.2f} - ${precio_max:.2f}")
    except ValueError:
        print("❌ Por favor ingresa valores numéricos válidos.")


def obtener_estadisticas():
    """
    Muestra estadísticas de la lista usando diccionarios
    """
    if not articulos:
        print("\n❌ La lista está vacía.")
        return
    
    # Crear diccionario con estadísticas
    estadisticas = {
        "total_articulos": len(articulos),
        "total_items": sum(art["cantidad"] for art in articulos),
        "precio_promedio": sum(art["precio"] for art in articulos) / len(articulos),
        "precio_minimo": min(art["precio"] for art in articulos),
        "precio_maximo": max(art["precio"] for art in articulos),
        "costo_total": sum(art["precio"] * art["cantidad"] for art in articulos)
    }
    
    print("\n--- ESTADÍSTICAS DE LA LISTA ---")
    print(f"Total de artículos distintos: {estadisticas['total_articulos']}")
    print(f"Total de items (cantidad): {estadisticas['total_items']}")
    print(f"Precio promedio: ${estadisticas['precio_promedio']:.2f}")
    print(f"Precio mínimo: ${estadisticas['precio_minimo']:.2f}")
    print(f"Precio máximo: ${estadisticas['precio_maximo']:.2f}")
    print(f"Costo total de compra: ${estadisticas['costo_total']:.2f}")


def modificar_articulo():
    """
    Modifica la cantidad de un artículo existente
    """
    if not articulos:
        print("\n❌ La lista está vacía.")
        return
    
    mostrar_articulos()
    
    try:
        numero = int(input("\nIngresa el número del artículo a modificar: "))
        if 1 <= numero <= len(articulos):
            articulo = articulos[numero - 1]  # Acceder al diccionario
            print(f"\nProducto actual: {articulo['producto']}")
            print(f"Cantidad actual: {articulo['cantidad']}")
            
            nueva_cantidad = int(input("Nueva cantidad: "))
            if nueva_cantidad <= 0:
                print("❌ La cantidad debe ser mayor a 0.")
                return
            
            articulo["cantidad"] = nueva_cantidad  # Modificar diccionario
            print(f"✅ Cantidad actualizada correctamente.")
        else:
            print(f"❌ Número inválido. Debe estar entre 1 y {len(articulos)}.")
    except ValueError:
        print("❌ Por favor ingresa un número válido.")


def menu_principal():
    """
    Muestra el menú principal y gestiona las opciones
    """
    while True:
        print("\n" + "="*50)
        print("    GESTOR DE LISTA DE COMPRAS")
        print("="*50)
        print("1. Agregar artículo")
        print("2. Ver lista de compras")
        print("3. Buscar producto")
        print("4. Filtrar por precio")
        print("5. Ver estadísticas")
        print("6. Modificar cantidad")
        print("7. Eliminar artículo")
        print("8. Limpiar lista")
        print("9. Salir")
        print("="*50)
        
        opcion = input("Selecciona una opción (1-9): ").strip()
        
        if opcion == "1":
            agregar_articulo()
        elif opcion == "2":
            mostrar_articulos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            filtrar_por_precio()
        elif opcion == "5":
            obtener_estadisticas()
        elif opcion == "6":
            modificar_articulo()
        elif opcion == "7":
            eliminar_articulo()
        elif opcion == "8":
            limpiar_lista()
        elif opcion == "9":
            print("\n👋 ¡Gracias por usar el Gestor de Compras!")
            break
        else:
            print("❌ Opción inválida. Por favor, selecciona una opción entre 1 y 9.")


# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()
