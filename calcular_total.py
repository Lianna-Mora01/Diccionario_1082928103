"""
Calcular Total de Compra
Programa que recorre una lista de diccionarios y calcula el total
acumulando precio × cantidad para cada artículo
"""

# Lista de artículos de compra (diccionarios)
articulos = [
    {"producto": "Leche", "precio": 2.50, "cantidad": 2},
    {"producto": "Pan", "precio": 1.50, "cantidad": 3},
    {"producto": "Queso", "precio": 5.00, "cantidad": 1},
    {"producto": "Manzanas", "precio": 0.80, "cantidad": 6},
    {"producto": "Huevos", "precio": 3.00, "cantidad": 1},
    {"producto": "Mantequilla", "precio": 4.20, "cantidad": 2},
    {"producto": "Yogur", "precio": 1.80, "cantidad": 4},
]

print("="*70)
print("           CALCULAR TOTAL DE COMPRA")
print("="*70)

# Variable para acumular el total
total_compra = 0

# Encabezados de la tabla
print(f"\n{'Nº':<3} {'Producto':<20} {'Precio Unit.':<15} {'Cantidad':<10} {'Subtotal':<12}")
print("-" * 70)

# MÉTODO 1: Recorrer lista y acumular totales
print("\n--- MÉTODO 1: Recorrido simple con acumulación ---\n")

for i, articulo in enumerate(articulos, 1):
    # Extraer datos del diccionario
    producto = articulo["producto"]
    precio = articulo["precio"]
    cantidad = articulo["cantidad"]
    
    # Calcular subtotal para este artículo
    subtotal = precio * cantidad
    
    # Acumular en el total general
    total_compra += subtotal
    
    # Mostrar datos del artículo
    print(f"{i:<3} {producto:<20} ${precio:<14.2f} {cantidad:<10} ${subtotal:<11.2f}")

print("-" * 70)
print(f"\n{'TOTAL GENERAL':<33} ${total_compra:.2f}\n")


# MÉTODO 2: Usar .items() para recorrer y calcular
print("="*70)
print("--- MÉTODO 2: Usando .items() para mostrar cada valor ---\n")

total_compra2 = 0
articulos_detalles = []

for i, articulo in enumerate(articulos, 1):
    # Usar .items() para obtener clave-valor
    datos_articulo = {}
    for clave, valor in articulo.items():
        datos_articulo[clave] = valor
    
    # Extraer valores
    subtotal = datos_articulo["precio"] * datos_articulo["cantidad"]
    total_compra2 += subtotal
    
    # Guardar información para mostrar
    articulos_detalles.append({
        "numero": i,
        "producto": datos_articulo["producto"],
        "precio": datos_articulo["precio"],
        "cantidad": datos_articulo["cantidad"],
        "subtotal": subtotal
    })

# Mostrar tabla
for item in articulos_detalles:
    print(f"{item['numero']:<3} {item['producto']:<20} ${item['precio']:<14.2f} "
          f"{item['cantidad']:<10} ${item['subtotal']:<11.2f}")

print("-" * 70)
print(f"TOTAL DE COMPRA: ${total_compra2:.2f}\n")


# MÉTODO 3: Calcular con list comprehension y sum()
print("="*70)
print("--- MÉTODO 3: Usando list comprehension ---\n")

# Calcular subtotales de todos los artículos de una vez
subtotales = [art["precio"] * art["cantidad"] for art in articulos]
total_compra3 = sum(subtotales)

print(f"Total general calculado: ${total_compra3:.2f}\n")

# Mostrar desglose
for i, (articulo, subtotal) in enumerate(zip(articulos, subtotales), 1):
    print(f"{i}. {articulo['producto']:<20} {articulo['cantidad']} x ${articulo['precio']:>6.2f} = ${subtotal:>8.2f}")

print("-" * 70)
print(f"TOTAL: ${sum(subtotales):.2f}\n")


# MÉTODO 4: Desglose detallado con .items()
print("="*70)
print("--- MÉTODO 4: Desglose detallado con .items() ---\n")

total_compra4 = 0

for i, articulo in enumerate(articulos, 1):
    print(f"Artículo {i}:")
    
    # Usar .items() para mostrar cada propiedad
    for clave, valor in articulo.items():
        if clave == "precio":
            print(f"  • Precio unitario: ${valor:.2f}")
        elif clave == "cantidad":
            print(f"  • Cantidad: {valor}")
        else:
            print(f"  • {clave.capitalize()}: {valor}")
    
    # Calcular y mostrar subtotal
    subtotal = articulo["precio"] * articulo["cantidad"]
    total_compra4 += subtotal
    print(f"  • Subtotal: ${subtotal:.2f}\n")

print("-" * 70)
print(f"TOTAL A PAGAR: ${total_compra4:.2f}\n")


# MÉTODO 5: Resumen con estadísticas
print("="*70)
print("--- MÉTODO 5: Resumen con Estadísticas ---\n")

# Recorrer y calcular estadísticas
precios = []
cantidades = []
total_compra5 = 0

for articulo in articulos:
    precio = articulo["precio"]
    cantidad = articulo["cantidad"]
    subtotal = precio * cantidad
    
    precios.append(precio)
    cantidades.append(cantidad)
    total_compra5 += subtotal

# Mostrar estadísticas
print(f"Total de artículos distintos: {len(articulos)}")
print(f"Cantidad total de items: {sum(cantidades)}")
print(f"Precio promedio por artículo: ${sum(precios) / len(precios):.2f}")
print(f"Precio más bajo: ${min(precios):.2f}")
print(f"Precio más alto: ${max(precios):.2f}")
print(f"\n{'='*70}")
print(f"MONTO TOTAL A PAGAR: ${total_compra5:.2f}")
print(f"{'='*70}\n")
