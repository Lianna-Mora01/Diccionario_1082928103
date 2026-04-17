"""
Ver Lista de Compras
Programa que itera sobre una lista de diccionarios
usando bucle for y .items()
"""

# Lista de artículos de compra (cada uno es un diccionario)
articulos = [
    {"producto": "Leche", "precio": 2.50, "cantidad": 2},
    {"producto": "Pan", "precio": 1.50, "cantidad": 3},
    {"producto": "Queso", "precio": 5.00, "cantidad": 1},
    {"producto": "Manzanas", "precio": 0.80, "cantidad": 6},
    {"producto": "Huevos", "precio": 3.00, "cantidad": 1},
]

print("="*60)
print("       VER LISTA DE COMPRAS USANDO .items()")
print("="*60)

# MÉTODO 1: Iterar sobre la lista con bucle for
print("\n--- MÉTODO 1: Acceso directo a diccionarios ---\n")

for i, articulo in enumerate(articulos, 1):
    print(f"Artículo {i}:")
    # Usar .items() para acceder a cada clave-valor
    for clave, valor in articulo.items():
        if clave == "precio":
            print(f"  {clave.capitalize()}: ${valor:.2f}")
        else:
            print(f"  {clave.capitalize()}: {valor}")
    print()


# MÉTODO 2: Tabla formateada usando .items()
print("\n" + "="*60)
print("--- MÉTODO 2: Tabla con formato ---\n")

print(f"{'Nº':<3} {'Producto':<20} {'Precio':<10} {'Cantidad':<10} {'Subtotal':<10}")
print("-" * 60)

total_general = 0

for i, articulo in enumerate(articulos, 1):
    # Usar .items() para extraer valores
    datos = {}
    for clave, valor in articulo.items():
        datos[clave] = valor
    
    producto = datos["producto"]
    precio = datos["precio"]
    cantidad = datos["cantidad"]
    subtotal = precio * cantidad
    total_general += subtotal
    
    print(f"{i:<3} {producto:<20} ${precio:<9.2f} {cantidad:<10} ${subtotal:<9.2f}")

print("-" * 60)
print(f"{'TOTAL':<33} ${total_general:.2f}\n")


# MÉTODO 3: Mostrar detalles con .items() y valores específicos
print("="*60)
print("--- MÉTODO 3: Detalles de cada artículo ---\n")

for i, articulo in enumerate(articulos, 1):
    print(f"📦 Artículo {i}:")
    
    # Iterar usando .items() para obtener claves y valores
    for clave, valor in articulo.items():
        if clave == "producto":
            print(f"   Nombre: {valor}")
        elif clave == "precio":
            print(f"   Valor unitario: ${valor:.2f}")
        elif clave == "cantidad":
            print(f"   Cantidad a comprar: {valor} unidades")
    
    # Calcular subtotal
    subtotal = articulo["precio"] * articulo["cantidad"]
    print(f"   Subtotal: ${subtotal:.2f}\n")


# MÉTODO 4: Filtrar usando .items()
print("="*60)
print("--- MÉTODO 4: Productos con precio mayor a $2 ---\n")

print(f"{'Producto':<20} {'Precio':<10} {'Cantidad':<10}")
print("-" * 40)

for articulo in articulos:
    # Usar .items() para acceder a los valores
    for clave, valor in articulo.items():
        if clave == "precio" and valor > 2.0:
            # Si el precio es mayor a $2, mostrar el artículo completo
            producto = articulo["producto"]
            precio = articulo["precio"]
            cantidad = articulo["cantidad"]
            print(f"{producto:<20} ${precio:<9.2f} {cantidad:<10}")
            break


# MÉTODO 5: Búsqueda de artículo específico
print("\n" + "="*60)
print("--- MÉTODO 5: Información completa de un producto ---\n")

producto_buscado = "Queso"

for articulo in articulos:
    # Usar .items() para iterar y buscar
    for clave, valor in articulo.items():
        if clave == "producto" and valor == producto_buscado:
            print(f"✅ Producto encontrado: {producto_buscado}\n")
            
            # Mostrar todos los detalles usando .items()
            for k, v in articulo.items():
                if k == "precio":
                    print(f"  {k.capitalize()}: ${v:.2f}")
                else:
                    print(f"  {k.capitalize()}: {v}")
            break

print("\n" + "="*60)
