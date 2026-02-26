from logica_poo import GestorInventario

mi_tienda = GestorInventario()

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

                nom_articulo = input("¿Qué artículo quieres vender? ").lower()
                cant_articulo = int(input("¿Cuántos quieres vender? "))
    
                # Aquí está la magia: el objeto se encarga de todo
                resultado = mi_tienda.vender(nom_articulo, cant_articulo)
    
                if resultado is not False:
                    mi_tienda.guardar_datos()
                    print(f"Venta exitosa. Stock restante: {resultado}")
                else:
                    print("Error en la venta.")
            
            case "2":
                print("Categorías existentes:")
                for cat in mi_tienda._categorias:
                    print(cat.capitalize())
                
                nueva_cat: str = input("Qué categoría deseas añadir? ")
                mi_tienda.n_categoria(nueva_cat)
                mi_tienda.guardar_datos()
                print("Categoría añadida")
            
            case "3":
                total_stock: float = mi_tienda.calcular_total()
                print(f"El total del valor del stock es: {total_stock}€")
    

if __name__ == "__main__":
    main()
