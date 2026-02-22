from inventario_logica import venta
from inventario_logica import n_categoria
from inventario_logica import valor_stock

# Diccionario de productos (Base de datos local)
productos: dict = {
    "monitor": {
        "precio": 150.0, 
        "stock": 10
    },
    "raton": {
        "precio": 25.0, 
        "stock": 45
    },
    "teclado": {
        "precio": 50.0, 
        "stock": 30
    }
}

# Set de categorías (Elementos únicos)
categorias: set = {"Periféricos", "Imagen"}

def main():
    while True:
        print("--- CONTROL DE STOCK Y VENTAS ---")
        print("¿Qué quieres hacer?\n1. Vender\n2. Añadir categoría\n3. Calcular valor de stock\n4. Salir")
        opcion = input(">")
        match opcion:
            case "4":
                break

            case "1":
                print("Artículos en venta y cantidad en stock")
                for articulo in productos:
                    print(articulo, "- ", productos[articulo]["stock"])
                try:
                    nom_articulo = input("¿Qué artículo quieres vender? ")
                    if nom_articulo not in productos:
                        print("El artículo no existe en el sistema.")
                        continue
                    cant_articulo = int(input("¿Cuántos quieres vender? "))
                except ValueError:
                    print("Los datos entregados no son correctos, la venta no ha finalizado correctamente.")
                    continue
                if cant_articulo > 0:
                    venta(productos, nom_articulo, cant_articulo)
                    print("Venta finalizada")
                else:
                    print("no se puede vender cantidades negativas.")
                    continue
            
            case "2":
                print("Categorías existentes:")
                for cat in categorias:
                    print(cat.capitalize())
                
                nueva_cat: str = input("Qué categoría deseas añadir? ")
                n_categoria(categorias, nueva_cat.lower())
                print("Categoría añadida")
            
            case "3":
                total_stock: float = valor_stock(productos)
                print(f"El total del valor del stock es: {total_stock}€")


if __name__ == "__main__":
    main()
