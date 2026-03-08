# --- ZONA DE PRUEBAS ---
from logica_biblioteca import Libro, Usuario, Biblioteca

# 1. Creamos la Biblioteca
mi_biblioteca = Biblioteca("Biblioteca Municipal")

mi_biblioteca.cargar_datos()

def main():
    # . INTENTO DE PRÉSTAMO
    print("\n--- Intento de préstamo 1 ---")
    mi_biblioteca.prestar("111", "12345X")

    # . COMPROBACIÓN FINAL
    print("\n--- Estado después del préstamo ---")
    print(mi_biblioteca.catalogo["111"])  # Debería decir [Prestado]
    print(f"Libros en poder de {mi_biblioteca.usuarios["12345X"].nombre}: {mi_biblioteca.usuarios["12345X"].libros_en_prestamo}")

    mi_biblioteca.guardar_datos()

if __name__ == "__main__":
    main()