# --- SOLICITUD DE DATOS ---
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Qué edad tienes? "))
saldo = float(input("¿Cuánto dinero tienes? "))
pase_vip = input("¿Tienes pase VIP? (si/no): ")

# --- LÓGICA DE DECISIÓN ---
# --- SOLUCIÓN LÓGICA PERO NO RECOMENDADA ---
# Al tener un "if" sobre otro no es una buena prácica. Se le llama solución anidada y es mejor evitarlo por que la acumulación dificulta la lectura.
# if pase_vip == "si":
#    print(f"¡Bienvenido {nombre}! Pase directo al área VIP.")
# else:
#    if edad < 18:
#       print(f"Lo siento {nombre}, eres menor de edad y no puedes pasar")
#    elif saldo < 50:
#       print(f"Lo siento {nombre}, tienes la edad pero no tienes dinero suficiente para la entrada")
#    else:
#       print(f"¡Bienvenido {nombre}! Disfruta del evento.")

# --- SOLUCIÓN RECOMENDADA ---
if pase_vip == "si":
    print(f"¡Bienvenido {nombre}! Pase directo al área VIP.")
elif edad >= 18 and saldo >= 50:
    print(f"¡Bienvenido {nombre}! Disfruta del evento.")
elif edad < 18:
    print(f"Lo siento {nombre}, eres menor de edad.")
else:
    print(f"Lo siento {nombre}, no tienes saldo suficiente.")