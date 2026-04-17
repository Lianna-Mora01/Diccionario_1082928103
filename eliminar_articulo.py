"""
Eliminar Artículo de la Lista de Compras
Programa que busca un producto específico por nombre 
y lo elimina de la lista usando remove()
"""

# Lista de artículos de compra
articulos = [
    {"producto": "Leche", "precio": 2.50, "cantidad": 2},
    {"producto": "Pan", "precio": 1.50, "cantidad": 3},
    {"producto": "Queso", "precio": 5.00, "cantidad": 1},
    {"producto": "Manzanas", "precio": 0.80, "cantidad": 6},
    {"producto": "Huevos", "precio": 3.00, "cantidad": 1},
    {"producto": "Mantequilla", "precio": 4.20, "cantidad": 2},
    {"producto": "Yogur", "precio": 1.80, "cantidad": 4},
]

def mostrar_lista():
    """
    Muestra todos los artículos actuales
    """
    print("\n--- LISTA DE COMPRAS ACTUAL ---\n")
    if not articulos:
        print("❌ La lista está vacía.\n")
        return
    
    print(f"{'Nº':<3} {'Producto':<20} {'Precio':<10} {'Cantidad':<10}")
    print("-" * 45)
    
    for i, art in enumerate(articulos, 1):
        print(f"{i:<3} {art['producto']:<20} ${art['precio']:<9.2f} {art['cantidad']:<10}")
    
    print(f"\nTotal de artículos: {len(articulos)}\n")


def eliminar_articulo_por_nombre():
    """
    MÉTODO 1: Elimina un artículo buscando por nombre exacto
    Usa remove() para eliminar el diccionario de la lista
    """
    print("\n" + "="*50)
    print("MÉTODO 1: Eliminar por nombre exacto")
    print("="*50)
    
    mostrar_lista()
    
    producto_buscar = input("Ingresa el nombre del producto a eliminar: ").strip()
    
    if not producto_buscar:
        print("❌ Debes ingesar un nombre válido.\n")
        return
    
    # Buscar el diccionario que contiene ese producto
    articulo_encontrado = None
    for art in articulos:
        if art["producto"].lower() == producto_buscar.lower():
            articulo_encontrado = art
            break
    
    if articulo_encontrado:
        # Usar remove() para eliminar el diccionario de la lista
        articulos.remove(articulo_encontrado)
        print(f"\n✅ '{articulo_encontrado['producto']}' eliminado correctamente.")
        print(f"   Precio: ${articulo_encontrado['precio']:.2f}")
        print(f"   Cantidad: {articulo_encontrado['cantidad']}\n")
    else:
        print(f"\n❌ No se encontró el producto '{producto_buscar}'.\n")


def eliminar_articulo_por_posicion():
    """
    MÉTODO 2: Elimina por posición (número)
    """
    print("\n" + "="*50)
    print("MÉTODO 2: Eliminar por número de posición")
    print("="*50)
    
    mostrar_lista()
    
    try:
        numero = int(input("Ingresa el número del artículo a eliminar: "))
        
        if 1 <= numero <= len(articulos):
            # pop() también elimina pero retorna el elemento
            articulo_eliminado = articulos.pop(numero - 1)
            print(f"\n✅ Artículo eliminado: {articulo_eliminado['producto']}")
            print(f"   Precio: ${articulo_eliminado['precio']:.2f}")
            print(f"   Cantidad: {articulo_eliminado['cantidad']}\n")
        else:
            print(f"\n❌ Número inválido. Debe estar entre 1 y {len(articulos)}.\n")
    except ValueError:
        print("❌ Por favor ingresa un número válido.\n")


def eliminar_por_filtro():
    """
    MÉTODO 3: Elimina todos los artículos de una categoría o precio
    """
    print("\n" + "="*50)
    print("MÉTODO 3: Eliminar por filtro (precio máximo)")
    print("="*50)
    
    mostrar_lista()
    
    try:
        precio_maximo = float(input("Ingresa el precio máximo para eliminar: $"))
        
        # Crear lista de artículos a eliminar
        articulos_a_eliminar = [art for art in articulos if art["precio"] <= precio_maximo]
        
        if articulos_a_eliminar:
            print(f"\n🗑️  Se eliminarán {len(articulos_a_eliminar)} artículos:\n")
            for art in articulos_a_eliminar:
                print(f"   • {art['producto']} - ${art['precio']:.2f}")
            
            # Usar remove() para cada artículo
            for art in articulos_a_eliminar:
                articulos.remove(art)
            
            print(f"\n✅ {len(articulos_a_eliminar)} artículos eliminados.\n")
        else:
            print(f"\n❌ No hay artículos con precio <= ${precio_maximo}.\n")
    except ValueError:
        print("❌ Por favor ingresa un precio válido.\n")


def eliminar_con_confirmacion():
    """
    MÉTODO 4: Elimina con confirmación del usuario
    """
    print("\n" + "="*50)
    print("MÉTODO 4: Eliminar con confirmación")
    print("="*50)
    
    mostrar_lista()
    
    producto_buscar = input("Ingresa el nombre del producto a eliminar: ").strip()
    
    # Buscar el artículo
    articulo_encontrado = None
    for art in articulos:
        if art["producto"].lower() == producto_buscar.lower():
            articulo_encontrado = art
            break
    
    if articulo_encontrado:
        print(f"\n📦 Producto encontrado:")
        print(f"   Nombre: {articulo_encontrado['producto']}")
        print(f"   Precio: ${articulo_encontrado['precio']:.2f}")
        print(f"   Cantidad: {articulo_encontrado['cantidad']}")
        
        confirmacion = input("\n¿Deseas eliminar este artículo? (s/n): ").lower()
        
        if confirmacion == 's':
            articulos.remove(articulo_encontrado)
            print(f"\n✅ '{articulo_encontrado['producto']}' eliminado correctamente.\n")
        else:
            print("\n❌ Operación cancelada.\n")
    else:
        print(f"\n❌ No se encontró el producto '{producto_buscar}'.\n")


def mostrar_menu():
    """
    Menú interactivo
    """
    while True:
        print("\n" + "="*50)
        print("    ELIMINAR ARTÍCULOS DE COMPRA")
        print("="*50)
        print("1. Ver lista actual")
        print("2. Eliminar por nombre exacto")
        print("3. Eliminar por número")
        print("4. Eliminar por filtro de precio")
        print("5. Eliminar con confirmación")
        print("6. Salir")
        print("="*50)
        
        opcion = input("Selecciona una opción (1-6): ").strip()
        
        if opcion == "1":
            mostrar_lista()
        elif opcion == "2":
            if articulos:
                eliminar_articulo_por_nombre()
            else:
                print("\n❌ La lista está vacía.\n")
        elif opcion == "3":
            if articulos:
                eliminar_articulo_por_posicion()
            else:
                print("\n❌ La lista está vacía.\n")
        elif opcion == "4":
            if articulos:
                eliminar_por_filtro()
            else:
                print("\n❌ La lista está vacía.\n")
        elif opcion == "5":
            if articulos:
                eliminar_con_confirmacion()
            else:
                print("\n❌ La lista está vacía.\n")
        elif opcion == "6":
            print("\n👋 ¡Hasta luego!\n")
            break
        else:
            print("\n❌ Opción inválida.\n")


# Ejecutar el programa
if __name__ == "__main__":
    mostrar_menu()
