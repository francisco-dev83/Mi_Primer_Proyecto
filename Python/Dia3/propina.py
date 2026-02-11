# --- ENTRADA DE DATOS ---
total_cuenta = float(input("¿Cuánto es el total dela cuenta? "))
numero_personas = int(input("¿Cuántas personas sois? "))
porcentaje_propina = int(input("¿Qué porcentaje de propina queréis dejar? "))

# --- CÁLCULOS ---
total_final = (total_cuenta + (total_cuenta * porcentaje_propina / 100)) / numero_personas

# --- SALIDA DE DATOS ---
print(f"Cada persona debe pagar {total_final:.2f} euros")