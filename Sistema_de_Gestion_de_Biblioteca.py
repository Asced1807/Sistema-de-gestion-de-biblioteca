# Elvin Coronado Reyes (Asce)
# creacion de la clase libro
class Libro:
    def __init__(self, titulo, autor, isbn, cantidad_copias):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.cantidad_copias = cantidad_copias
        self.prestamos_activos = []
# creacion de las funciones 
    def agregar_libro(self, cantidad):
        self.cantidad_copias += cantidad

    def prestamo_devolucion(self, usuario, accion):
        if accion == "prestamo":
            if self.cantidad_copias > 0:
                self.cantidad_copias -= 1
                self.prestamos_activos.append(usuario)
                print(f"Libro '{self.titulo}' prestado a {usuario}.")
            else:
                print("No quedan copias disponibles para préstamo.")
        elif accion == "devolucion":
            if usuario in self.prestamos_activos:
                self.cantidad_copias += 1
                self.prestamos_activos.remove(usuario)
                print(f"Libro '{self.titulo}' devuelto por {usuario}.")
            else:
                print(f"{usuario} no tiene este libro prestado.")

    def buscar_libros(self, criterio, disponible_para_prestamo=False):
        libros_encontrados = []
        if criterio.lower() in self.titulo.lower() or criterio.lower() in self.autor.lower():
            if disponible_para_prestamo:
                if self.cantidad_copias > len(self.prestamos_activos):
                    libros_encontrados.append(self)
            else:
                libros_encontrados.append(self)
        return libros_encontrados

def generar_reportes(libros):
    if not libros:
        print("No hay libros en la biblioteca para generar reportes.")
        return

    # Libro más prestado
    libro_mas_prestado = max(libros, key=lambda libro: len(libro.prestamos_activos))
    print(f"\nLibro más prestado: {libro_mas_prestado.titulo}, Prestado {len(libro_mas_prestado.prestamos_activos)} veces.")

    # Libro menos prestado
    libro_menos_prestado = min(libros, key=lambda libro: len(libro.prestamos_activos))
    print(f"Libro menos prestado: {libro_menos_prestado.titulo}, Prestado {len(libro_menos_prestado.prestamos_activos)} veces.")

    # Autor con más libros en la biblioteca
    autores_contador = {}
    for libro in libros:
        if libro.autor in autores_contador:
            autores_contador[libro.autor] += 1
        else:
            autores_contador[libro.autor] = 1
    autor_mas_libros = max(autores_contador, key=autores_contador.get)
    print(f"Autor con más libros en la biblioteca: {autor_mas_libros}, {autores_contador[autor_mas_libros]} libros.")


# Función para mostrar el menú y realizar las acciones
def mostrar_menu():
    print("\nBiblioteca ElvinDEV")
    print("\n1. Agregar Libro")
    print("2. Realizar Préstamo")
    print("3. Realizar Devolución")
    print("4. Buscar Libros")
    print("5. Generar Reportes Estadísticos")
    print("6. Eliminar Libro")
    print("7. Actualizar Libro")
    print("8. Salir")
    opcion = input("\nSeleccione una opción: ")
    return opcion

# aqui tenemos las condiciones para ejecutar segun la opcion seleccionada
if __name__ == "__main__":
    libros = []

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            cantidad = int(input("Ingrese la cantidad de copias disponibles: "))
            libros.append(Libro(titulo, autor, isbn, cantidad))
            print("Libro agregado con éxito.")

        elif opcion == "2":
            usuario = input("Ingrese el nombre del usuario: ")
            criterio_busqueda = input("Ingrese título o autor del libro a prestar: ")
            for libro in libros:
                resultados_busqueda = libro.buscar_libros(criterio_busqueda, True)
                if resultados_busqueda:
                    libro = resultados_busqueda[0]  # Tomamos el primer resultado encontrado
                    libro.prestamo_devolucion(usuario, "prestamo")
                    print("Libro prestado con exito")
                    break
            else:
                print("No se encontraron libros disponibles para préstamo.")

        elif opcion == "3":
            usuario = input("Ingrese el nombre del usuario: ")
            criterio_busqueda = input("Ingrese título o autor del libro a devolver: ")
            for libro in libros:
                resultados_busqueda = libro.buscar_libros(criterio_busqueda)
                if resultados_busqueda:
                    libro = resultados_busqueda[0]  # Tomamos el primer resultado encontrado
                    libro.prestamo_devolucion(usuario, "devolucion")
                    print("Devolucion con exito")
                    break
            else:
                print(f"{usuario} no tiene este libro prestado.")

        elif opcion == "4":
            print("\nInventario de Libros:")
            for idx, libro in enumerate(libros, start=1):
                print(f"{idx}. Título: {libro.titulo}, Autor: {libro.autor}, Copias Disponibles: {libro.cantidad_copias}")

            criterio_busqueda = input("\nSeleccione una opción para buscar libros:\n1. Buscar por Título\n2. Buscar por Autor\nOpción: ")
            if criterio_busqueda == "1":
                criterio = input("Ingrese el título del libro a buscar: ")
                resultados_busqueda = []
                for libro in libros:
                    resultados_busqueda.extend(libro.buscar_libros(criterio))
                if resultados_busqueda:
                    print("Resultados de búsqueda:")
                    for libro in resultados_busqueda:
                        print(f"Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}, Copias Disponibles: {libro.cantidad_copias}")
                else:
                    print("No se encontraron libros que coincidan con la búsqueda.")
            elif criterio_busqueda == "2":
                criterio = input("Ingrese el autor del libro a buscar: ")
                resultados_busqueda = []
                for libro in libros:
                    resultados_busqueda.extend(libro.buscar_libros(criterio))
                if resultados_busqueda:
                    print("Resultados de búsqueda:")
                    for libro in resultados_busqueda:
                        print(f"Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}, Copias Disponibles: {libro.cantidad_copias}")
                else:
                    print("No se encontraron libros que coincidan con la búsqueda.")
            else:
                print("Opción no válida.")

        elif opcion == "5":
            generar_reportes(libros)

        elif opcion == "6":
            criterio_busqueda = input("Ingrese título o autor del libro a eliminar: ")
            libro_encontrado = None
            for libro in libros:
                resultados_busqueda = libro.buscar_libros(criterio_busqueda)
                if resultados_busqueda:
                    libro_encontrado = resultados_busqueda[0]
                    libros.remove(libro_encontrado)
                    print(f"Libro '{libro_encontrado.titulo}' eliminado con éxito.")
                    break
            if libro_encontrado is None:
                print("No se encontraron libros que coincidan con la búsqueda.")

        elif opcion == "7":
            criterio_busqueda = input("Ingrese título o autor del libro a actualizar: ")
            libro_encontrado = None
            for libro in libros:
                resultados_busqueda = libro.buscar_libros(criterio_busqueda)
                if resultados_busqueda:
                    libro_encontrado = resultados_busqueda[0]
                    print(f"Libro encontrado:\nTítulo: {libro_encontrado.titulo}, Autor: {libro_encontrado.autor}, ISBN: {libro_encontrado.isbn}, Copias Disponibles: {libro_encontrado.cantidad_copias}")
                    cantidad_a_agregar = int(input("Ingrese la cantidad de copias a agregar: "))
                    libro_encontrado.cantidad_copias += cantidad_a_agregar
                    print(f"Copias disponibles actualizadas a {libro_encontrado.cantidad_copias}.")
                    break
            if libro_encontrado is None:
                print("No se encontraron libros que coincidan con la búsqueda.")

        elif opcion == "8":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")




