"""
=========================================================
SISTEMA DE GESTIÓN DE TIENDA DE VIDEOJUEGOS
=========================================================

Descripción:
Sistema de consola para administrar el inventario y las
ventas de una tienda de videojuegos.

Funcionalidades:
- Agregar videojuegos
- Mostrar inventario
- Buscar videojuegos
- Actualizar precios
- Registrar ventas
- Mostrar estadísticas
- Eliminar videojuegos
- Historial de ventas
- Videojuego más vendido

Requerimientos:
- Python 3.x

Dependencias:
- Ninguna (solo librerías estándar)

Autor:
Estudiante Python

Ejecución:
python tienda_videojuegos.py

=========================================================
"""


# =========================================================
# DATOS INICIALES DE PRUEBA
# =========================================================

diccionario_videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10,
        "vendidos": 0
    },
    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5,
        "vendidos": 0
    },
    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8,
        "vendidos": 0
    }
}

lista_historial_ventas = []


# =========================================================
# FUNCIÓN AGREGAR VIDEOJUEGO
# =========================================================
def agregar_videojuego(diccionario_videojuegos):
    """
    Permite registrar un nuevo videojuego.

    Parámetros:
        diccionario_videojuegos (dict)

    Retorna:
        None
    """

    print("\n===== AGREGAR VIDEOJUEGO =====")

    codigo_videojuego = input("Ingrese código: ").upper()

    if codigo_videojuego in diccionario_videojuegos:
        print("Error: El código ya existe.")
        return

    nombre_videojuego = input("Ingrese nombre: ")
    nombre_plataforma = input("Ingrese plataforma: ")

    try:
        precio_videojuego = float(input("Ingrese precio: "))
        cantidad_inventario = int(input("Ingrese cantidad: "))

        if precio_videojuego <= 0:
            print("El precio debe ser mayor que cero.")
            return

        if cantidad_inventario <= 0:
            print("La cantidad debe ser mayor que cero.")
            return

        diccionario_videojuegos[codigo_videojuego] = {
            "nombre": nombre_videojuego,
            "plataforma": nombre_plataforma,
            "precio": precio_videojuego,
            "cantidad": cantidad_inventario,
            "vendidos": 0
        }

        print("Videojuego agregado correctamente.")

    except ValueError:
        print("Debe ingresar valores numéricos válidos.")


# =========================================================
# FUNCIÓN MOSTRAR INVENTARIO
# =========================================================
def mostrar_inventario(diccionario_videojuegos):
    """
    Muestra todos los videojuegos registrados.

    Parámetros:
        diccionario_videojuegos (dict)

    Retorna:
        None
    """

    print("\n===== INVENTARIO =====")

    if len(diccionario_videojuegos) == 0:
        print("No existen videojuegos registrados.")
        return

    for codigo_videojuego, datos_videojuego in diccionario_videojuegos.items():

        print("-" * 50)
        print(f"Código: {codigo_videojuego}")
        print(f"Nombre: {datos_videojuego['nombre']}")
        print(f"Plataforma: {datos_videojuego['plataforma']}")
        print(f"Precio: ${datos_videojuego['precio']:,.0f}")
        print(f"Cantidad: {datos_videojuego['cantidad']}")
        print(f"Vendidos: {datos_videojuego['vendidos']}")


# =========================================================
# FUNCIÓN BUSCAR VIDEOJUEGO
# =========================================================
def buscar_videojuego(diccionario_videojuegos):
    """
    Busca un videojuego por código.

    Parámetros:
        diccionario_videojuegos (dict)

    Retorna:
        None
    """

    codigo_videojuego = input(
        "\nIngrese código a buscar: "
    ).upper()

    if codigo_videojuego in diccionario_videojuegos:

        datos_videojuego = diccionario_videojuegos[codigo_videojuego]

        print("\nVideojuego encontrado")
        print(f"Nombre: {datos_videojuego['nombre']}")
        print(f"Plataforma: {datos_videojuego['plataforma']}")
        print(f"Precio: ${datos_videojuego['precio']:,.0f}")
        print(f"Cantidad: {datos_videojuego['cantidad']}")

    else:
        print("Videojuego no encontrado.")


# =========================================================
# FUNCIÓN ACTUALIZAR PRECIO
# =========================================================
def actualizar_precio(diccionario_videojuegos):
    """
    Actualiza el precio de un videojuego.

    Parámetros:
        diccionario_videojuegos (dict)

    Retorna:
        None
    """

    codigo_videojuego = input(
        "\nIngrese código del videojuego: "
    ).upper()

    if codigo_videojuego not in diccionario_videojuegos:
        print("Videojuego no encontrado.")
        return

    try:
        nuevo_precio = float(
            input("Ingrese nuevo precio: ")
        )

        if nuevo_precio <= 0:
            print("Precio inválido.")
            return

        diccionario_videojuegos[codigo_videojuego]["precio"] = nuevo_precio

        print("Precio actualizado correctamente.")

    except ValueError:
        print("Debe ingresar un valor numérico válido.")


# =========================================================
# FUNCIÓN REGISTRAR VENTA
# =========================================================
def registrar_venta(
        diccionario_videojuegos,
        lista_historial_ventas):
    """
    Registra la venta de un videojuego.

    Parámetros:
        diccionario_videojuegos (dict)
        lista_historial_ventas (list)

    Retorna:
        None
    """

    codigo_videojuego = input(
        "\nIngrese código del videojuego: "
    ).upper()

    if codigo_videojuego not in diccionario_videojuegos:
        print("Videojuego no encontrado.")
        return

    try:
        cantidad_vendida = int(
            input("Ingrese cantidad a vender: ")
        )

        if cantidad_vendida <= 0:
            print("Cantidad inválida.")
            return

        cantidad_disponible = (
            diccionario_videojuegos[codigo_videojuego]["cantidad"]
        )

        if cantidad_vendida > cantidad_disponible:
            print("Inventario insuficiente.")
            return

        precio_unitario = (
            diccionario_videojuegos[codigo_videojuego]["precio"]
        )

        valor_subtotal = precio_unitario * cantidad_vendida

        porcentaje_descuento = 0

        if valor_subtotal > 500000:
            porcentaje_descuento = valor_subtotal * 0.10

        valor_total = valor_subtotal - porcentaje_descuento

        diccionario_videojuegos[codigo_videojuego]["cantidad"] -= cantidad_vendida

        diccionario_videojuegos[codigo_videojuego]["vendidos"] += cantidad_vendida

        lista_historial_ventas.append({
            "codigo": codigo_videojuego,
            "cantidad": cantidad_vendida,
            "total": valor_total
        })

        print("\n===== FACTURA =====")
        print(
            f"Juego: "
            f"{diccionario_videojuegos[codigo_videojuego]['nombre']}"
        )
        print(f"Cantidad: {cantidad_vendida}")
        print(f"Precio Unitario: ${precio_unitario:,.0f}")
        print(f"Subtotal: ${valor_subtotal:,.0f}")
        print(f"Descuento: ${porcentaje_descuento:,.0f}")
        print(f"TOTAL: ${valor_total:,.0f}")

    except ValueError:
        print("Debe ingresar un número válido.")


# =========================================================
# FUNCIÓN ESTADÍSTICAS
# =========================================================
def mostrar_estadisticas(diccionario_videojuegos):
    """
    Muestra estadísticas generales.

    Parámetros:
        diccionario_videojuegos (dict)

    Retorna:
        None
    """

    if len(diccionario_videojuegos) == 0:
        print("No existen datos.")
        return

    total_videojuegos = len(diccionario_videojuegos)

    valor_total_inventario = 0
    suma_precios = 0

    videojuego_costoso = None
    videojuego_mayor_stock = None

    precio_mayor = 0
    cantidad_mayor = 0

    for codigo_videojuego, datos_videojuego in diccionario_videojuegos.items():

        valor_total_inventario += (
            datos_videojuego["precio"] *
            datos_videojuego["cantidad"]
        )

        suma_precios += datos_videojuego["precio"]

        if datos_videojuego["precio"] > precio_mayor:
            precio_mayor = datos_videojuego["precio"]
            videojuego_costoso = datos_videojuego["nombre"]

        if datos_videojuego["cantidad"] > cantidad_mayor:
            cantidad_mayor = datos_videojuego["cantidad"]
            videojuego_mayor_stock = datos_videojuego["nombre"]

    promedio_precios = suma_precios / total_videojuegos

    print("\n===== ESTADÍSTICAS =====")
    print(f"Total videojuegos: {total_videojuegos}")
    print(f"Valor inventario: ${valor_total_inventario:,.0f}")
    print(f"Juego más costoso: {videojuego_costoso}")
    print(f"Mayor inventario: {videojuego_mayor_stock}")
    print(f"Promedio precios: ${promedio_precios:,.0f}")


# =========================================================
# FUNCIÓN ELIMINAR VIDEOJUEGO
# =========================================================
def eliminar_videojuego(diccionario_videojuegos):
    """
    Elimina un videojuego por código.

    Parámetros:
        diccionario_videojuegos (dict)

    Retorna:
        None
    """

    codigo_videojuego = input(
        "\nIngrese código a eliminar: "
    ).upper()

    if codigo_videojuego in diccionario_videojuegos:
        del diccionario_videojuegos[codigo_videojuego]
        print("Videojuego eliminado.")
    else:
        print("Código no encontrado.")


# =========================================================
# FUNCIÓN INVENTARIO BAJO
# =========================================================
def mostrar_inventario_bajo(diccionario_videojuegos):
    """
    Muestra videojuegos con inventario menor a 3.

    Parámetros:
        diccionario_videojuegos (dict)

    Retorna:
        None
    """

    print("\n===== INVENTARIO BAJO =====")

    for codigo_videojuego, datos_videojuego in diccionario_videojuegos.items():

        if datos_videojuego["cantidad"] < 3:
            print(
                codigo_videojuego,
                datos_videojuego["nombre"],
                datos_videojuego["cantidad"]
            )


# =========================================================
# FUNCIÓN VIDEOJUEGO MÁS VENDIDO
# =========================================================
def mostrar_mas_vendido(diccionario_videojuegos):
    """
    Muestra el videojuego con mayor cantidad vendida.

    Parámetros:
        diccionario_videojuegos (dict)

    Retorna:
        None
    """

    nombre_mas_vendido = ""
    cantidad_vendida = -1

    for datos_videojuego in diccionario_videojuegos.values():

        if datos_videojuego["vendidos"] > cantidad_vendida:

            cantidad_vendida = datos_videojuego["vendidos"]
            nombre_mas_vendido = datos_videojuego["nombre"]

    print("\n===== VIDEOJUEGO MÁS VENDIDO =====")
    print(nombre_mas_vendido)
    print(f"Cantidad vendida: {cantidad_vendida}")


# =========================================================
# FUNCIÓN MENÚ
# =========================================================
def menu():
    """
    Muestra el menú principal.

    Parámetros:
        Ninguno

    Retorna:
        None
    """

    while True:

        print("\n")
        print("=" * 45)
        print("===== TIENDA DE VIDEOJUEGOS =====")
        print("=" * 45)
        print("1. Agregar videojuego")
        print("2. Mostrar inventario")
        print("3. Buscar videojuego")
        print("4. Actualizar precio")
        print("5. Registrar venta")
        print("6. Mostrar estadísticas")
        print("7. Eliminar videojuego")
        print("8. Inventario bajo")
        print("9. Videojuego más vendido")
        print("10. Salir")

        opcion_usuario = input(
            "\nSeleccione una opción: "
        )

        if opcion_usuario == "1":
            agregar_videojuego(diccionario_videojuegos)

        elif opcion_usuario == "2":
            mostrar_inventario(diccionario_videojuegos)

        elif opcion_usuario == "3":
            buscar_videojuego(diccionario_videojuegos)

        elif opcion_usuario == "4":
            actualizar_precio(diccionario_videojuegos)

        elif opcion_usuario == "5":
            registrar_venta(
                diccionario_videojuegos,
                lista_historial_ventas
            )

        elif opcion_usuario == "6":
            mostrar_estadisticas(diccionario_videojuegos)

        elif opcion_usuario == "7":
            eliminar_videojuego(diccionario_videojuegos)

        elif opcion_usuario == "8":
            mostrar_inventario_bajo(diccionario_videojuegos)

        elif opcion_usuario == "9":
            mostrar_mas_vendido(diccionario_videojuegos)

        elif opcion_usuario == "10":
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opción inválida.")


# ==========================================
# INICIO DEL PROGRAMA
# ==========================================

print("Iniciando sistema de gestión de videojuegos...\n")

menu()