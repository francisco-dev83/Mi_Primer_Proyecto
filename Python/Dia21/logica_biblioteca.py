import json
import os

class Libro:
    def __init__(self, titulo, autor, isbn, formato, genero):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.formato = formato
        self.genero = genero
        self.prestado = False  # Por defecto, está en la biblioteca

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"{self.titulo} ({self.autor}) - [{estado}]"
    
    def to_dict(self):
        # Convertimos el objeto en un diccionario simple
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "isbn": self.isbn,
            "formato": self.formato,
            "genero": self.genero,
            "prestado": self.prestado
        }

class Usuario:
    def __init__(self, dni, nombre, apellidos, edad, es_socio=True):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.es_socio = es_socio
        self.libros_en_prestamo = []  # Aquí guardaremos los ISBN de lo que se lleve

    def __str__(self):
        return f"{self.nombre} {self.apellidos} (DNI: {self.dni})"
    
    def to_dict(self):
        return {
            "dni": self.dni,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "edad": self.edad,
            "es_socio": self.es_socio,
            "libros_en_prestamo": self.libros_en_prestamo
        }

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = {}  # { "ISBN": ObjetoLibro }
        self.usuarios = {}  # { "DNI": ObjetoUsuario }

    def registrar_libro(self, libro_nuevo):
        # libro_nuevo es un objeto de la clase Libro
        # Lo guardamos usando su ISBN como llave
        self.catalogo[libro_nuevo.isbn] = libro_nuevo
        print(f"Libro '{libro_nuevo.titulo}' registrado en el sistema.")

    def registrar_usuario(self, usuario_nuevo):
        # Lo mismo con el usuario y su DNI
        self.usuarios[usuario_nuevo.dni] = usuario_nuevo
        print(f"Usuario {usuario_nuevo.nombre} dado de alta.")
    
    def prestar(self, isbn, dni):
        libro = self.catalogo.get(isbn)
        usuario = self.usuarios.get(dni)
        if libro and usuario and not libro.prestado:
            libro.prestado = True
            usuario.libros_en_prestamo.append(isbn)
            print(f"El usuario {usuario.nombre} se lleva {libro.titulo}.")
        else:
            print("No se puede realizar el préstamo")
    
    def devolver(self, isbn):
        libro = self.catalogo.get(isbn)
        
        if not libro:
            print("Ese ISBN no existe en nuestro catálogo")
            return
        if not libro.prestado:
            print(f"El libro '{libro.titulo}' ya está en la estantería.")
            return
        
        for u in self.usuarios.values():
            if isbn in u.libros_en_prestamo:
                u.libros_en_prestamo.remove(isbn)
                libro.prestado = False
                print(f"Libro {isbn} devuelto con éxito.")
                return

    def guardar_datos(self):
        datos = {
            "libros": {},
            "usuarios": {}
        }

        # Convertimos todos los libros
        for isbn, obj_libro in self.catalogo.items():
            datos["libros"][isbn] = obj_libro.to_dict()

        # Convertimos todos los usuarios
        for dni, obj_usuario in self.usuarios.items():
            datos["usuarios"][dni] = obj_usuario.to_dict()

        with open("data_biblioteca.json", "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        
        print("💾 Datos guardados correctamente en data_biblioteca.json")
    
    def cargar_datos(self):
        if os.path.exists("data_biblioteca.json"):
            print(f"Buscando el archivo en: {os.path.abspath("data_biblioteca.json")}")
            with open("data_biblioteca.json", "r", encoding="utf-8") as f:
                datos = json.load(f)
 
                # 1. RECONSTRUIR LIBROS
                for isbn, d in datos["libros"].items():
                    # Creamos un objeto Libro real con los datos del diccionario
                    obj_libro = Libro(d['titulo'], d['autor'], d['isbn'], d['formato'], d['genero'])
                    # No olvides el estado del préstamo, que no va en el __init__
                    obj_libro.prestado = d['prestado']
                    # Lo guardamos en el catálogo
                    self.catalogo[isbn] = obj_libro
                
                # 2. RECONSTRUIR USUARIOS
                for dni, d in datos["usuarios"].items():
                    # Creamos un objeto Usuario real
                    obj_usuario = Usuario(d['dni'], d['nombre'], d['apellidos'], d['edad'], d['es_socio'])
                    # Le devolvemos su lista de libros
                    obj_usuario.libros_en_prestamo = d['libros_en_prestamo']
                    # Lo guardamos en el diccionario de usuarios
                    self.usuarios[dni] = obj_usuario
        else:
            # Datos por defecto si el archivo no existe
            # 2. Creamos un par de Libros y un Usuario
            libro_1 = Libro("Cien años de soledad", "García Márquez", "111", "Papel", "Realismo Mágico")
            libro_2 = Libro("Python Crash Course", "Eric Matthes", "222", "Digital", "Tecnología")
            usuario_1 = Usuario("12345X", "Francisco", "Pérez", 30)

            # 3. Registramos todo en la Biblioteca
            self.registrar_libro(libro_1)
            self.registrar_libro(libro_2)
            self.registrar_usuario(usuario_1)
