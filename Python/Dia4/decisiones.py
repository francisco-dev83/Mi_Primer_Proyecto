total_cuenta = float(input("Total de la cuenta: "))
num_personas = int(input("¿Cuántas personas sois? "))

if num_personas > 0:
    pago_individual = total_cuenta / num_personas
    print(f"Cada uno debe pagar {pago_individual:.2f} euros.")
else:
    print("Error: El número de personas debe ser mayor que 0.")