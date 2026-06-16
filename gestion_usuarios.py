from datetime import datetime

# Archivo donde se almacenan los usuarios válidos
ARCHIVO_USUARIOS = "usuarios.txt"

# Archivo donde se almacenan los errores encontrados
ARCHIVO_ERRORES = "errores.txt"

# --------------------------------------------------
# Verifica si un usuario ya existe
# --------------------------------------------------
def usuario_existe(nombre_buscado):
    try:
        with open(ARCHIVO_USUARIOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) >= 1:
                    nombre = datos[0]
                    if nombre.lower() == nombre_buscado.lower():
                        return True
        return False
    except FileNotFoundError:
        return False

# --------------------------------------------------
# Guarda errores encontrados en el archivo de errores
# --------------------------------------------------
def registrar_error(registro, mensaje):
    with open(ARCHIVO_ERRORES, "a", encoding="utf-8") as archivo:
        archivo.write(registro + " --> " + mensaje + "\n")

# --------------------------------------------------
# Registrar usuario
# --------------------------------------------------
def registrar_usuario():
    try:
        nombre = input("Ingrese el nombre del usuario: ").strip()
        if nombre == "":
            print("\n Error: El nombre no puede estar vacío.")
            return
        if usuario_existe(nombre):
            print("\n Error: El usuario ya se encuentra registrado.")
            return
        edad = int(input("Ingrese la edad del usuario: "))
        if edad < 0:
            print("\n Error: La edad no puede ser negativa.")
            return
        if edad > 120:
            print("\n Error: La edad está fuera del rango, es superior a 120 años.")
            return
        from datetime import datetime
        fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(ARCHIVO_USUARIOS, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{edad},{fecha_creacion}\n")
        print("\n" + "=" * 110)
        print(f"{'NOMBRE':<20}{'EDAD':<10}{'FECHA CREACIÓN':<25}{'OBSERVACION'}")
        print("=" * 110)
        print(f"{nombre:<20}"f"{edad:<10}"f"{fecha_creacion:<25}"f"{'Registro almacenado exitosamente'}")
        print("=" * 110)
    except ValueError:
        print("\n Error: La edad debe ser numérica.")
    except PermissionError:
        print("\n Error: No se tienen permisos para escribir en el archivo.")
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")

# --------------------------------------------------
# Mostrar usuarios
# --------------------------------------------------
def mostrar_usuarios():
    suma_edades = 0
    cantidad_edades = 0
    try:
        with open(ARCHIVO_USUARIOS, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                print("No hay usuarios registrados.")
                return
            total_registros = 0
            print("\n" + "=" * 110)
            print(f"{'NOMBRE':<20}{'EDAD':<10}{'FECHA CREACIÓN':<25}{'OBSERVACION'}")
            print("=" * 110)
            total_registros = 0
            suma_edades = 0
            usuarios_validos = 0
            for numero, linea in enumerate(lineas, start=1):
                total_registros += 1
                error = ""
                datos = linea.strip().split(",")
                if len(datos) != 3:
                    error = "Cantidad incorrecta de campos"
                    registrar_error(linea.strip(),error)
                    nombre = "N/A"
                    edad = "N/A"
                    fecha = "N/A"
                else:
                    nombre, edad, fecha = datos
                    if nombre.strip() == "":
                        error = "Nombre vacío"
                    try:
                        edad_num = int(edad)
                        if edad_num >= 0 and edad_num <= 120:
                            suma_edades += edad_num
                            cantidad_edades += 1
                        elif edad_num < 0:
                            error = "Edad inferior a cero"
                        elif edad_num > 120:
                            error = "Edad fuera de rango, es superior a 120 años"
                    except ValueError:
                        error = "Edad no numérica"
                    if error != "":
                        registrar_error(linea.strip(),error)
                print(f"{nombre:<20}"f"{edad:<10}"f"{fecha:<25}"f"{error}")
            print("=" * 110)
            print(f"Total de registros: {total_registros}")
            if cantidad_edades > 0:
                promedio = suma_edades / cantidad_edades
                print(f"Promedio de edades: {promedio:.2f}")
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")
    except PermissionError:
        print("No se tienen permisos para leer el archivo.")
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")

# --------------------------------------------------
# Buscar usuario por nombre
# --------------------------------------------------
def buscar_usuario():
    try:
        nombre_buscar = input("Ingrese el nombre del usuario a buscar: ").strip()
        usuarios_encontrados = []
        with open(ARCHIVO_USUARIOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) == 3:
                    nombre, edad, fecha = datos
                    if nombre.lower() == nombre_buscar.lower():
                        error = ""
                        if nombre.strip() == "":
                            error = "Nombre vacío"
                        try:
                            edad_num = int(edad)
                            if edad_num < 0:
                                error = "Edad negativa"
                            elif edad_num > 120:
                                error = "Edad fuera de rango, es superior a 120 años"
                        except ValueError:
                            error = "Edad no numérica"
                        usuarios_encontrados.append(
                            [nombre, edad, fecha, error]
                        )
        if len(usuarios_encontrados) == 0:
            print(f"\nNo se encontró ningún usuario con el nombre '{nombre_buscar}'.")
        else:
            print("\n" + "=" * 110)
            print(f"{'NOMBRE':<20}{'EDAD':<10}{'FECHA CREACIÓN':<25}{'OBSERVACION'}")
            print("=" * 110)
            for usuario in usuarios_encontrados:
                print(f"{usuario[0]:<20}"f"{usuario[1]:<10}"f"{usuario[2]:<25}"f"{usuario[3]}")
            print("=" * 110)
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")
    except PermissionError:
        print("No se tienen permisos para leer el archivo.")
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")

# --------------------------------------------------
# Eliminar usuario por nombre
# --------------------------------------------------
def eliminar_usuario():
    try:
        nombre_eliminar = input("Ingrese el nombre del usuario a eliminar: ").strip()
        usuarios = []
        encontrado = False
        with open(ARCHIVO_USUARIOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) == 3:
                    nombre, edad, fecha = datos
                    if nombre.lower() == nombre_eliminar.lower():
                        encontrado = True
                    else:
                        usuarios.append(linea)
        if encontrado:
            with open(ARCHIVO_USUARIOS, "w", encoding="utf-8") as archivo:
                for usuario in usuarios:
                    archivo.write(usuario)
            print("\nUsuario eliminado exitosamente.")
            mostrar_usuarios()
        else:
            print("\nNo se encontró el usuario.")
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")
    except PermissionError:
        print("No se tienen permisos sobre el archivo.")
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")

# --------------------------------------------------
# Ordenar usuario por nombre
# --------------------------------------------------
def ordenar_usuarios():
    try:
        usuarios = []
        with open(ARCHIVO_USUARIOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) == 3:
                    nombre, edad, fecha = datos
                    usuarios.append([nombre, edad, fecha])
        if len(usuarios) == 0:
            print("No hay usuarios registrados.")
            return
        print("\nORDENAR POR")
        print("1. Nombre")
        print("2. Edad")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            usuarios.sort(key=lambda usuario: usuario[0].lower())
        elif opcion == "2":
            usuarios.sort(key=lambda usuario: int(usuario[1]))
        else:
            print("Opción no válida.")
            return

        # Guardar nuevamente el archivo ordenado
        with open(ARCHIVO_USUARIOS, "w", encoding="utf-8") as archivo:
            for usuario in usuarios:
                archivo.write(f"{usuario[0]},{usuario[1]},{usuario[2]}\n")
        print("\nUsuarios ordenados exitosamente.")
        print("\n" + "=" * 110)
        print(f"{'NOMBRE':<20}{'EDAD':<10}{'FECHA CREACIÓN':<25}{'OBSERVACION'}")
        print("=" * 110)
        for usuario in usuarios:
            print(f"{usuario[0]:<20}"f"{usuario[1]:<10}"f"{usuario[2]:<25}")
        print("=" * 110)
        print(f"Total de registros: {len(usuarios)}")
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")
    except PermissionError:
        print("No se tienen permisos para acceder al archivo.")
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")

# --------------------------------------------------
# Mostrar archivo de errores
# --------------------------------------------------
def mostrar_errores():
    try:
        with open(ARCHIVO_ERRORES, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                print("No hay errores registrados.")
                return
            total_errores = 0
            print("\n" + "=" * 120)
            print(f"{'NOMBRE':<20}{'EDAD':<10}{'FECHA CREACIÓN':<25}{'OBSERVACION'}")
            print("=" * 120)
            for linea in lineas:
                total_errores += 1
                partes = linea.strip().split("-->")
                if len(partes) == 2:
                    registro = partes[0].strip()
                    error = partes[1].strip()
                    datos = registro.split(",")
                    if len(datos) == 3:
                        nombre, edad, fecha = datos
                    else:
                        nombre = "N/A"
                        edad = "N/A"
                        fecha = "N/A"
                    print(f"{nombre:<20}"f"{edad:<10}"f"{fecha:<25}"f"{error}")
            print("=" * 120)
            print(f"Total de errores: {total_errores}")
    except FileNotFoundError:
        print("No existe el archivo de errores.")
    except PermissionError:
        print("No se tienen permisos para leer el archivo.")
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")

# --------------------------------------------------
# Menú principal
# --------------------------------------------------
def menu():
    opcion = ""
    while opcion != "7":
        print("\n===== MENÚ =====")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios - (Cantidad y Promedio)")
        print("3. Buscar usuario")
        print("4. Eliminar usuario")
        print("5. Ordenar usuario - (Nombre o Edad)")
        print("6. Mostrar Archivo de Errores")
        print("7. Salir")
        print("")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            buscar_usuario()
        elif opcion == "4":
            eliminar_usuario()
        elif opcion == "5":
            ordenar_usuarios()
        elif opcion == "6":
            mostrar_errores()
        elif opcion == "7":
            print("Programa finalizado.")
        else:
            print("Opción no válida.")

# Inicio del programa
menu()