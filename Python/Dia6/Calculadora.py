def sumar(a: float, b: float) -> float:
    return a + b
def restar(a: float, b:float) -> float:
    return a - b
def multiplicar(a: float, b: float) -> float:
    return a * b
def dividir(a: float, b: float) -> float:
    if b <= 0:
        return 0
    else:
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
            print(f"El resultado es: {c}")
        
        if opcion == "4":
            a = float(input("Dame el dividendo: "))
            b = float(input("Dame el divisor: "))
            c = dividir(a, b)
            if c == 0:
                print("El divisor debe ser mayor a 0") 
            else:
                print(f"El resultado es: {c}")

if __name__ == "__main__":
    main()
