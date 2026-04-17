"""
Búsqueda en Lista
Programa que implementa cuatro funciones para trabajar con una lista de números:
- buscar_numero()
- numeros_mayores()
- promedio_lista()
- ordenar_lista()
"""

# Lista de números para trabajar
numeros = [12, 45, 78, 23, 56, 89, 34, 67]

def mostrar_lista():
    """
    Muestra la lista actual
    """
    print(f"\n📊 Lista actual: {numeros}\n")


def buscar_numero(numero):
    """
    FUNCIÓN 1: Busca un número en la lista
    Devuelve el índice del número, o -1 si no existe
    
    Método 1: Usando .index() con try-except
    Método 2: Usando un bucle for
    """
    print("\n" + "="*60)
    print("FUNCIÓN 1: BUSCAR NÚMERO")
    print("="*60)
    
    mostrar_lista()
    
    print("--- MÉTODO 1: Usando .index() ---\n")
    try:
        indice = numeros.index(numero)
        print(f"✅ '{numero}' encontrado en la posición {indice}")
        print(f"   Elemento: {numeros[indice]}\n")
        return indice
    except ValueError:
        print(f"❌ '{numero}' no existe en la lista.\n")
        return -1


def buscar_numero_bucle(numero):
    """
    FUNCIÓN 1 (Alternativa): Buscar usando bucle for
    """
    print("\n--- MÉTODO 2: Usando bucle for ---\n")
    
    for i, num in enumerate(numeros):
        if num == numero:
            print(f"✅ '{numero}' encontrado en la posición {i}")
            print(f"   Elemento: {numeros[i]}\n")
            return i
    
    print(f"❌ '{numero}' no existe en la lista.\n")
    return -1


def numeros_mayores(umbral):
    """
    FUNCIÓN 2: Devuelve una nueva lista con todos los números mayores que el umbral
    
    Método 1: Usando list comprehension
    Método 2: Usando un bucle for
    """
    print("\n" + "="*60)
    print("FUNCIÓN 2: NÚMEROS MAYORES QUE UN UMBRAL")
    print("="*60)
    
    mostrar_lista()
    print(f"Umbral: {umbral}\n")
    
    print(f"--- MÉTODO 1: List comprehension ---\n")
    # Usar comprensión de listas para filtrar
    result_comprension = [num for num in numeros if num > umbral]
    print(f"Números mayores a {umbral}: {result_comprension}\n")
    
    print(f"--- MÉTODO 2: Usando bucle for ---\n")
    # Usar bucle for
    result_bucle = []
    for num in numeros:
        if num > umbral:
            result_bucle.append(num)
    
    print(f"Números mayores a {umbral}: {result_bucle}\n")
    
    if result_comprension:
        print(f"✅ Se encontraron {len(result_comprension)} números mayores a {umbral}\n")
    else:
        print(f"❌ No hay números mayores a {umbral}\n")
    
    return result_comprension


def promedio_lista(lista):
    """
    FUNCIÓN 3: Calcula y devuelve el promedio de todos los elementos
    Usa sum() y len() para simplificar el cálculo
    """
    print("\n" + "="*60)
    print("FUNCIÓN 3: PROMEDIO DE LA LISTA")
    print("="*60)
    
    if not lista:
        print("\n❌ La lista está vacía.\n")
        return 0
    
    print(f"\n📋 Lista: {lista}\n")
    
    print("--- Cálculo del promedio ---\n")
    
    # Calcular suma
    suma = sum(lista)
    print(f"Suma: {' + '.join(map(str, lista))} = {suma}")
    
    # Contar elementos
    cantidad = len(lista)
    print(f"Cantidad de elementos: {cantidad}")
    
    # Calcular promedio
    promedio = suma / cantidad
    print(f"\nPromedio = Suma / Cantidad")
    print(f"Promedio = {suma} / {cantidad}")
    print(f"Promedio = {promedio:.2f}\n")
    
    print(f"✅ El promedio es: {promedio:.2f}\n")
    return promedio


def ordenar_lista(lista):
    """
    FUNCIÓN 4: Ordena los números de menor a mayor
    
    Método 1: Usando sorted() - devuelve nueva lista
    Método 2: Usando .sort() - modifica la lista original
    """
    print("\n" + "="*60)
    print("FUNCIÓN 4: ORDENAR LISTA")
    print("="*60)
    
    print(f"\n📋 Lista original: {lista}\n")
    
    print("--- MÉTODO 1: Usando sorted() ---\n")
    lista_ordenada_sorted = sorted(lista)
    print(f"Lista ordenada: {lista_ordenada_sorted}")
    print("(sorted() devuelve una nueva lista, no modifica la original)\n")
    
    print("--- MÉTODO 2: Usando .sort() ---\n")
    lista_copia = lista.copy()  # Hacer copia para no modificar original
    lista_copia.sort()
    print(f"Lista ordenada: {lista_copia}")
    print("(.sort() modifica la lista original)\n")
    
    print(f"✅ Lista ordenada de menor a mayor: {lista_ordenada_sorted}\n")
    return lista_ordenada_sorted


def ordenar_descendente(lista):
    """
    FUNCIÓN 4 (Alternativa): Ordenar de mayor a menor
    """
    print("\n--- MÉTODO 3: Ordenar descendente ---\n")
    lista_descendente = sorted(lista, reverse=True)
    print(f"Lista ordenada (mayor a menor): {lista_descendente}\n")
    return lista_descendente


def menu_principal():
    """
    Menú interactivo para invocar las funciones
    """
    while True:
        print("\n" + "="*60)
        print("      BÚSQUEDA Y MANIPULACIÓN DE LISTAS")
        print("="*60)
        print("\n1. Ver lista actual")
        print("2. Buscar un número")
        print("3. Números mayores que un umbral")
        print("4. Calcular promedio")
        print("5. Ordenar la lista")
        print("6. Ordenar descendente (mayor a menor)")
        print("7. Salir")
        print("="*60)
        
        opcion = input("\nSelecciona una opción (1-7): ").strip()
        
        try:
            if opcion == "1":
                mostrar_lista()
            
            elif opcion == "2":
                numero_buscar = int(input("\nIngresa el número a buscar: "))
                buscar_numero(numero_buscar)
                input("\nPresiona Enter para continuar...")
                
                otra = input("¿Ver el método alternativo (bucle)? (s/n): ").lower()
                if otra == 's':
                    buscar_numero_bucle(numero_buscar)
                    input("\nPresiona Enter para continuar...")
            
            elif opcion == "3":
                umbral = int(input("\nIngresa el umbral: "))
                numeros_mayores(umbral)
                input("Presiona Enter para continuar...")
            
            elif opcion == "4":
                promedio_lista(numeros)
                input("Presiona Enter para continuar...")
            
            elif opcion == "5":
                ordenar_lista(numeros)
                input("Presiona Enter para continuar...")
            
            elif opcion == "6":
                ordenar_descendente(numeros)
                input("Presiona Enter para continuar...")
            
            elif opcion == "7":
                print("\n👋 ¡Hasta luego!\n")
                break
            
            else:
                print("\n❌ Opción inválida. Intenta de nuevo.\n")
        
        except ValueError:
            print("❌ Por favor ingresa un valor numérico válido.\n")


def ejemplo_completo():
    """
    Ejecuta un ejemplo completo mostrando todas las funciones
    """
    print("\n" + "="*60)
    print("      EJEMPLO COMPLETO DE TODAS LAS FUNCIONES")
    print("="*60)
    
    mostrar_lista()
    
    # Ejemplo 1: Buscar
    print("\n--- EJEMPLO 1: Buscando el número 45 ---")
    indice = buscar_numero(45)
    
    # Ejemplo 2: Números mayores
    print("\n--- EJEMPLO 2: Números mayores a 50 ---")
    mayores = numeros_mayores(50)
    
    # Ejemplo 3: Promedio
    print("\n--- EJEMPLO 3: Promedio de la lista ---")
    prom = promedio_lista(numeros)
    
    # Ejemplo 4: Ordenar
    print("\n--- EJEMPLO 4: Lista ordenada ---")
    ordenada = ordenar_lista(numeros)
    
    print("\n" + "="*60)
    print("           RESUMEN DE RESULTADOS")
    print("="*60)
    print(f"\n✅ Número 45 encontrado en índice: {indice}")
    print(f"✅ Números mayores a 50: {mayores}")
    print(f"✅ Promedio: {prom:.2f}")
    print(f"✅ Lista ordenada: {ordenada}\n")


# Ejecutar el programa
if __name__ == "__main__":
    print("\n¿Deseas ejecutar un ejemplo completo o usar el menú interactivo?\n")
    print("1. Ejemplo completo")
    print("2. Menú interactivo")
    
    opcion = input("\nSelecciona (1 o 2): ").strip()
    
    if opcion == "1":
        ejemplo_completo()
    else:
        menu_principal()
