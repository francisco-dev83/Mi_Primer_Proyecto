def sumar(a: float, b: float) -> float:
    """Suma dos números reales
    
    Args:
        a (float): Primer sumando
        b (float): Segundo sumando
    
    Returns:
        Float: devuelve la suma de ambos números."""
    return a + b
def restar(a: float, b:float) -> float:
    """Resta dos números reales
    
    Args:
        a (float): El minuendo
        b (float): El sustraendo
    
    Returns:
        Float: devuelve la resta de ambos números."""
    return a - b
def multiplicar(a: float, b: float) -> float:
    """Multiplica dos números reales
    
    Args:
        a (float): Primer factor
        b (float): Segundo factor
    
    Returns:
        Float: devuelve la multiplicación de ambos números."""
    return a * b
def dividir(a: float, b: float) -> float:
    """Divide dos números reales
    
    Args:
        a (float): El dividendo
        b (float): El divisor
    
    Returns:
        Float: El cociente o None si el divisor es cero
    """
    if b == 0:
        return None
    return a / b

def main():
     # Declaración de variables globales
    historial: list[float] = []
        
    while True:
        # Declaración variables locales
        opcion : str = ""
        a: float = 0.0
        b: float = 0.0
        resultado: float | None = 0.0

        # Presentación de la calculadora
        print("\n--- CALCULADORA MODULAR---")
        print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Historial\n6. Salir")
        opcion = input("Elige una opción: ")

        # Lógica del código
        match opcion:
            case "6":
                print("Saliendo...")
                break

            case "1" | "2" | "3" | "4":
                try:
                    a = float(input("Primer número: "))
                    b = float(input("Segundo número: "))
                except ValueError:
                    print("Error: Por favor, introduce sólo números válidos.")
                    continue


                match opcion:
                    case "1":
                        resultado = sumar(a,b)
                    
                    case "2":
                        resultado = restar(a,b)
                    
                    case "3":
                        resultado = multiplicar(a,b)
                    
                    case "4":
                        resultado = dividir(a,b)
                

                if resultado is None:
                    print("No se puede dividir por 0")
                else:
                    print(f"Resultado: {resultado}")
                    historial.append(resultado)


            case "5":
                 for i, valor in enumerate(historial, start = 1):
                    print(f"Operación {i}: {valor}")
            
            case _:
                print("Opción no válida, inténtalo de nuevo.")
        
if __name__ == "__main__":
    main()
