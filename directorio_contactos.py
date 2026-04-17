"""
Directorio de Contactos
Programa que gestiona un directorio de contactos usando un diccionario de diccionarios
Estructura: { "nombre": { "email": "...", "teléfono": "...", "ciudad": "..." } }
"""

# Diccionario principal de contactos
contactos = {
    "Juan Pérez": {
        "email": "juan@email.com",
        "teléfono": "555-1234",
        "ciudad": "Madrid"
    },
    "María García": {
        "email": "maria@email.com",
        "teléfono": "555-5678",
        "ciudad": "Barcelona"
    },
    "Carlos López": {
        "email": "carlos@email.com",
        "teléfono": "555-9012",
        "ciudad": "Valencia"
    },
}


def agregar_contacto():
    """
    FUNCIÓN 1: Agregar un nuevo contacto
    Solicita nombre, email, teléfono y ciudad
    Crea la entrada en el diccionario principal
    """
    print("\n" + "="*60)
    print("FUNCIÓN 1: AGREGAR CONTACTO")
    print("="*60 + "\n")
    
    nombre = input("Nombre del contacto: ").strip()
    
    # Verificar si ya existe
    if nombre in contactos:
        print(f"⚠️  ¡El contacto '{nombre}' ya existe!\n")
        return
    
    if not nombre:
        print("❌ El nombre no puede estar vacío.\n")
        return
    
    email = input("Email: ").strip()
    if not email:
        print("❌ El email no puede estar vacío.\n")
        return
    
    telefono = input("Teléfono: ").strip()
    if not telefono:
        print("❌ El teléfono no puede estar vacío.\n")
        return
    
    ciudad = input("Ciudad: ").strip()
    if not ciudad:
        print("❌ La ciudad no puede estar vacía.\n")
        return
    
    # Crear el diccionario del contacto y agregarlo
    contactos[nombre] = {
        "email": email,
        "teléfono": telefono,
        "ciudad": ciudad
    }
    
    print(f"\n✅ Contacto '{nombre}' agregado correctamente.\n")


def ver_todos_contactos():
    """
    FUNCIÓN 2: Ver todos los contactos
    Itera con .items() e imprime cada contacto de forma legible
    """
    print("\n" + "="*60)
    print("FUNCIÓN 2: VER TODOS LOS CONTACTOS")
    print("="*60 + "\n")
    
    if not contactos:
        print("❌ El directorio está vacío.\n")
        return
    
    print(f"{'Nº':<3} {'Nombre':<20} {'Email':<25} {'Teléfono':<12} {'Ciudad':<15}\n")
    print("-" * 85)
    
    # Iterar con .items() sobre el diccionario principal
    for i, (nombre, datos) in enumerate(contactos.items(), 1):
        # Acceder a cada campo del diccionario anidado
        email = datos["email"]
        telefono = datos["teléfono"]
        ciudad = datos["ciudad"]
        
        print(f"{i:<3} {nombre:<20} {email:<25} {telefono:<12} {ciudad:<15}")
    
    print(f"\n✅ Total de contactos: {len(contactos)}\n")


def ver_contactos_detallado():
    """
    FUNCIÓN 2 (alternativa): Ver todos los contactos con formato detallado
    """
    print("\n" + "="*60)
    print("VISTA DETALLADA DE CONTACTOS")
    print("="*60 + "\n")
    
    if not contactos:
        print("❌ El directorio está vacío.\n")
        return
    
    # Iterar con .items() mostrando formato detallado
    for i, (nombre, datos) in enumerate(contactos.items(), 1):
        print(f"📇 Contacto {i}:")
        print(f"   Nombre:   {nombre}")
        
        # Usar .items() en el diccionario anidado también
        for campo, valor in datos.items():
            campo_formateado = campo.capitalize()
            print(f"   {campo_formateado}: {valor}")
        print()
    
    print(f"✅ Total de contactos: {len(contactos)}\n")


def buscar_por_nombre():
    """
    FUNCIÓN 3: Buscar por nombre
    Pide un nombre y muestra sus datos
    Usa .get() para evitar errores si no existe
    """
    print("\n" + "="*60)
    print("FUNCIÓN 3: BUSCAR POR NOMBRE")
    print("="*60 + "\n")
    
    nombre_buscar = input("Ingresa el nombre a buscar: ").strip()
    
    # Usar .get() - devuelve None si no existe (no lanza error)
    contacto = contactos.get(nombre_buscar)
    
    if contacto:
        print(f"\n✅ Contacto encontrado: {nombre_buscar}\n")
        print(f"   📧 Email:    {contacto['email']}")
        print(f"   📱 Teléfono: {contacto['teléfono']}")
        print(f"   🏙️  Ciudad:   {contacto['ciudad']}\n")
    else:
        print(f"\n❌ No se encontró el contacto '{nombre_buscar}'.\n")
        print("💡 Contactos disponibles:")
        for nombre in contactos.keys():
            print(f"   • {nombre}")
        print()


def buscar_por_ciudad():
    """
    FUNCIÓN 3 (alternativa): Buscar contactos por ciudad
    """
    print("\n" + "="*60)
    print("BUSCAR CONTACTOS POR CIUDAD")
    print("="*60 + "\n")
    
    ciudad_buscar = input("Ingresa la ciudad a buscar: ").strip()
    
    # Filtrar contactos por ciudad
    resultados = []
    for nombre, datos in contactos.items():
        if datos["ciudad"].lower() == ciudad_buscar.lower():
            resultados.append((nombre, datos))
    
    if resultados:
        print(f"\n✅ Se encontraron {len(resultados)} contacto(s) en {ciudad_buscar}:\n")
        for nombre, datos in resultados:
            print(f"   • {nombre}: {datos['email']} ({datos['teléfono']})")
        print()
    else:
        print(f"\n❌ No hay contactos en {ciudad_buscar}.\n")


def actualizar_telefono():
    """
    FUNCIÓN 4: Actualizar teléfono
    Pide el nombre del contacto y el nuevo teléfono
    Accede al diccionario anidado y actualiza
    """
    print("\n" + "="*60)
    print("FUNCIÓN 4: ACTUALIZAR TELÉFONO")
    print("="*60 + "\n")
    
    nombre = input("Nombre del contacto: ").strip()
    
    # Usar .get() para verificar que existe
    if nombre not in contactos:
        print(f"❌ No se encontró el contacto '{nombre}'.\n")
        return
    
    # Mostrar teléfono actual
    telefono_actual = contactos[nombre]["teléfono"]
    print(f"\nTeléfono actual: {telefono_actual}")
    
    nuevo_telefono = input("Nuevo teléfono: ").strip()
    
    if not nuevo_telefono:
        print("❌ El teléfono no puede estar vacío.\n")
        return
    
    # Acceder al diccionario anidado y actualizar
    contactos[nombre]["teléfono"] = nuevo_telefono
    
    print(f"\n✅ Teléfono actualizado correctamente.")
    print(f"   Nuevo teléfono: {nuevo_telefono}\n")


def actualizar_contacto_completo():
    """
    FUNCIÓN 4 (alternativa): Actualizar cualquier campo del contacto
    """
    print("\n" + "="*60)
    print("ACTUALIZAR CONTACTO (CUALQUIER CAMPO)")
    print("="*60 + "\n")
    
    nombre = input("Nombre del contacto: ").strip()
    
    if nombre not in contactos:
        print(f"❌ No se encontró el contacto '{nombre}'.\n")
        return
    
    print(f"\n📇 Contacto actual: {nombre}")
    for campo, valor in contactos[nombre].items():
        print(f"   {campo.capitalize()}: {valor}")
    
    print("\nCampos disponibles para actualizar:")
    print("1. email")
    print("2. teléfono")
    print("3. ciudad")
    
    opcion = input("\nSelecciona el campo a actualizar (1-3): ").strip()
    
    campo_map = {"1": "email", "2": "teléfono", "3": "ciudad"}
    campo = campo_map.get(opcion)
    
    if not campo:
        print("❌ Opción inválida.\n")
        return
    
    nuevo_valor = input(f"Nuevo {campo}: ").strip()
    
    if not nuevo_valor:
        print(f"❌ El {campo} no puede estar vacío.\n")
        return
    
    contactos[nombre][campo] = nuevo_valor
    print(f"\n✅ {campo.capitalize()} actualizado correctamente.\n")


def eliminar_contacto():
    """
    FUNCIÓN 5: Eliminar contacto
    Pide el nombre y usa .pop() para eliminar la entrada completa
    """
    print("\n" + "="*60)
    print("FUNCIÓN 5: ELIMINAR CONTACTO")
    print("="*60 + "\n")
    
    nombre = input("Nombre del contacto a eliminar: ").strip()
    
    # Verificar si existe
    if nombre not in contactos:
        print(f"❌ No se encontró el contacto '{nombre}'.\n")
        return
    
    # Mostrar datos antes de eliminar
    datos = contactos[nombre]
    print(f"\n⚠️  Se eliminará el siguiente contacto:")
    print(f"   Nombre: {nombre}")
    print(f"   Email: {datos['email']}")
    print(f"   Teléfono: {datos['teléfono']}")
    print(f"   Ciudad: {datos['ciudad']}")
    
    confirmacion = input("\n¿Deseas eliminar este contacto? (s/n): ").lower()
    
    if confirmacion == 's':
        # Usar .pop() para eliminar la entrada completa del diccionario
        contacto_eliminado = contactos.pop(nombre)
        print(f"\n✅ Contacto '{nombre}' eliminado correctamente.\n")
    else:
        print("\n❌ Operación cancelada.\n")


def menu_principal():
    """
    Menú interactivo principal
    """
    while True:
        print("\n" + "="*60)
        print("    DIRECTORIO DE CONTACTOS")
        print("="*60)
        print("\n1. Agregar contacto")
        print("2. Ver todos los contactos")
        print("3. Ver contactos (formato detallado)")
        print("4. Buscar por nombre")
        print("5. Buscar por ciudad")
        print("6. Actualizar teléfono")
        print("7. Actualizar cualquier campo")
        print("8. Eliminar contacto")
        print("9. Salir")
        print("="*60)
        
        opcion = input("\nSelecciona una opción (1-9): ").strip()
        
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            ver_todos_contactos()
        elif opcion == "3":
            ver_contactos_detallado()
        elif opcion == "4":
            buscar_por_nombre()
        elif opcion == "5":
            buscar_por_ciudad()
        elif opcion == "6":
            actualizar_telefono()
        elif opcion == "7":
            actualizar_contacto_completo()
        elif opcion == "8":
            eliminar_contacto()
        elif opcion == "9":
            print("\n👋 ¡Hasta luego!\n")
            break
        else:
            print("\n❌ Opción inválida. Intenta de nuevo.\n")


# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()
