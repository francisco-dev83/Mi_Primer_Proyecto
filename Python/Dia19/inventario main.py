from logica_poo import GestorInventario

mi_tienda = GestorInventario()

def main():
    while True:
        print("--- CONTROL DE STOCK Y VENTAS ---")
        print("¿Qué quieres hacer?\n1. Vender\n2. Añadir categoría\n3. Calcular valor de stock\n4. Salir")
        opcion = input(">")
        match opcion:
            case "4":
                break

            case "1":
                print("Artículos existentes:")
                for art in mi_tienda._productos.keys():
                    print(art.capitalize())             
                   
                nom_articulo = input("¿Qué artículo quieres vender? ").lower()
                while True:
                    try:
                        cant_articulo = int(input("¿Cuántos quieres vender? "))
                        break  # <--- Si llega aquí es que el int() funcionó, así que salimos del "while True"
                    except ValueError:
                        print("❌ Número no válido. Inténtalo de nuevo.")
    
                resultado = mi_tienda.vender(nom_articulo, cant_articulo)
    
                if resultado is not False:
                    mi_tienda.guardar_datos()
                    mi_tienda.registrar_log(f"VENTA: {nom_articulo} - CANTIDAD: {cant_articulo}")
                    print(f"Venta exitosa. Stock restante: {resultado}")
                else:
                    mi_tienda.registrar_log(f"ERROR VENTA: {nom_articulo} - CANTIDAD : {cant_articulo}")
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
                moneda = input("En qué divisa quieres ver el resultado?")
                if moneda.upper() in ["EUR", ""]:
                    total_stock: float = mi_tienda.calcular_total()
                    print(f"El total del valor del stock es: {total_stock}€")
                else:
                    divisa = mi_tienda.calcular_total_divisa(moneda)
                    if divisa is None:
                        print("No se puede mostrar el valor en esa divisa")
                    else:
                        print(f"El total del valor del stock es: {divisa:.2f}")

if __name__ == "__main__":
    main()
