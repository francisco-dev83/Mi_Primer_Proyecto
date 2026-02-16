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
        a (float): El inuendo
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
    while True:
        print("\n--- CALCULADORA MODULAR---")
        print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "5":
            break 
        
        if opcion == "1":
            a = float(input("Dame el primer sumando: "))
            b = float(input("Dame el segundo sumando: "))
            c = sumar(a, b)
            print(f"El resultado es: {c}")
        
        if opcion == "2":
            a = float(input("Dame el minuendo: "))
            b = float(input("Dame el sustraendo: "))
            c = restar(a, b)
            print(f"El resultado es: {c}")
        
        if opcion == "3":
            a = float(input("Dame el primer factor: "))
            b = float(input("Dame el segundo factor: "))
            c = multiplicar(a,b)
            print(f"El resultado es: {c}")
        
        if opcion == "4":
            a = float(input("Dame el dividendo: "))
            b = float(input("Dame el divisor: "))
            c = dividir(a, b)
            if c is None:
                print("Error: El divisor deve ser diferente de 0") 
            else:
                print(f"El resultado es: {c}")

if __name__ == "__main__":
    main()
