import json
import os

# Obtenemos la ruta absoluta de la carpeta donde está ESTE archivo .py
RUTA_BASE = os.path.dirname(os.path.abspath(__file__))

# Creamos la ruta completa uniendo la carpeta con el nombre del archivo
ARCHIVO_JSON = os.path.join(RUTA_BASE, "biblioteca.json")


class Libro():
    def __init__(self, isbn, titulo, autor):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.usuario_actual = None

    def __str__(self):
        return f"ID: {self.isbn} | {self.titulo} de {self.autor}"
    
    def prestar(self, nombre_usuario):
        if self.usuario_actual is None:
            self.usuario_actual = nombre_usuario
        else:
            print("El libro ya está prestado")
    def devolver(self):
        if self.usuario_actual is not None:
            self.usuario_actual = None
        else:
            print("El libro ya se encuentra en la estantería")
    def estado_libro(self):
        return f"Prestado a {self.usuario_actual}" if self.usuario_actual is not None else "Disponible"
    
    def a_diccionario(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "usuario_actual": self.usuario_actual.id_socio if self.usuario_actual else None
        }


class Usuario():
    def __init__(self, id_socio, nombre):
        self.id_socio = id_socio
        self.nombre = nombre
        self.libros_en_mano = []
    
    def __str__(self):
        return f"Usuario {self.id_socio}: {self.nombre}"
    
    def a_diccionario(self):
        return {
            "id_socio": self.id_socio,
            "nombre": self.nombre,
            "libros_en_mano": [libro.isbn for libro in self.libros_en_mano]
        }


def buscar_y_prestar(isbn, id_usuario):
    if isbn in biblioteca.keys():
        if id_usuario in usuarios.keys():
            biblioteca[isbn].prestar(usuarios[id_usuario])
            usuarios[id_usuario].libros_en_mano.append(biblioteca[isbn])
            print("Libro prestado")
        else:
            print(f"El usuario con Id {id_usuario}, no se encuentra en el sistema")
    else:
        print(f"El libro con ISBN {isbn}, no se encuentra en el catálogo")

def buscar_y_devolver(isbn):
    if isbn in biblioteca:
        libro = biblioteca[isbn]
        user = libro.usuario_actual

        if user:
            libro.devolver()
            user.libros_en_mano.remove(libro)
        else:
            print("Éste libro ya se encuentra en la biblioteca.")
    else:
        print(f"El libro con ISBN {isbn}, no se encuentra en el catálogo")


def buscar_por_titulo(texto):
    encontrado = False
    for lib in biblioteca.values():
        if texto.lower() in lib.titulo.lower():
            print(f"Encontrado: {lib}")
            encontrado = True
    if not encontrado:
        print("No hay coincidencias con ese título.")

def guardar_datos():
    datos_para_guardar = {"libros": {isbn: lib.a_diccionario() for  isbn, lib in biblioteca.items()},
                          "usuarios": {id: user.a_diccionario() for id, user in usuarios.items()}}

    with open(ARCHIVO_JSON, "w") as archivo:
        json.dump(datos_para_guardar, archivo, indent=4)
        print("Datos guardados con éxito.")

def cargar_datos():
    global biblioteca, usuarios

    try:
        with open(ARCHIVO_JSON, "r") as archivo:
            datos = json.load(archivo)

            for id_s, d in datos["usuarios"].items():
                nuevo_usuario = Usuario(d["id_socio"], d["nombre"])
                usuarios[id_s] = nuevo_usuario
            
            for isbn, d in datos["libros"].items():
                nuevo_libro = Libro(d["isbn"], d["titulo"], d["autor"])
                biblioteca[isbn] = nuevo_libro
                id_user = d["usuario_actual"]
                if id_user:
                    objeto_usuario = usuarios[id_user]
                    nuevo_libro.usuario_actual = objeto_usuario
                    objeto_usuario.libros_en_mano.append(nuevo_libro)
                biblioteca[isbn] = nuevo_libro
        print("Memoria recuperada con éxito.")
    except FileNotFoundError:
        print("No se encontró el archivo de datos. Iniciando con datos por defecto")

        libro1 = Libro("978-01", "Cien años de soledad", "Gabriel García Márquez")
        libro2 = Libro("978-02", "1984", "George Orwell")
        libro3 = Libro("978-03", "El Principito", "Antoine de Saint-Exupéry")
        usuario1 = Usuario("S001", "Francisco")
        usuario2 = Usuario("S002", "Elena")
        usuario3 = Usuario("S003", "Miguel")

        biblioteca[libro1.isbn] = libro1
        biblioteca[libro2.isbn] = libro2
        biblioteca[libro3.isbn] = libro3
        usuarios[usuario1.id_socio] = usuario1
        usuarios[usuario2.id_socio] = usuario2
        usuarios[usuario3.id_socio] = usuario3


def limpiar_pantalla():
    # 'nt' es para Windows, 'posix' para Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')


biblioteca = {}
usuarios = {}

#buscar_y_prestar("978-02", "S001")
#print(biblioteca["978-02"].estado_libro())
#buscar_y_prestar("999-99", "Alguien")

#print("--- estado de los libros ---")

#for lib in biblioteca.values():
#    print(f"Libro {lib.titulo}: {lib.estado_libro()}")

#buscar_y_devolver("978-02")

#print("--- estado de los libros ---")

#for lib in biblioteca.values():
#    print(f"Libro {lib.titulo}: {lib.estado_libro()}")

def menu_principal():
    while True:
        print("--- GESTIÓN DE BIBLIOTECA ---")
        print("1. Ver catálogo completo")
        print("2. Buscar libro por título")
        print("3. Realizar préstamo")
        print("4. Devolver libro")
        print("5. Salir")
        opc = input("->")
        match opc:
            case "5":
                print("Saliendo del programa")
                break

            case "1":
                limpiar_pantalla()
                print("--- CATÁLOGO COMPLETO ---")
                for lib in biblioteca.values():
                    print(lib, " / ", lib.estado_libro())
            
            case "2":
                limpiar_pantalla()
                lib = input("¿Qué libro quieres buscar? ")
                buscar_por_titulo(lib)
            
            case "3":
                lib = input("Introduce el ISBN del libro: ")
                user = input("Introduce el Id del usuario: ")
                limpiar_pantalla()
                buscar_y_prestar(lib, user)
            
            case "4":
                lib = input("introduce el ISBN del libro: ")
                limpiar_pantalla()
                buscar_y_devolver(lib)
                print("Devolución completada.")

if __name__ == "__main__":
    limpiar_pantalla()
    cargar_datos()
    menu_principal()
    guardar_datos()

