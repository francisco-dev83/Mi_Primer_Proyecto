# Bucle FOR
# Queremos repetir algo 5 veces
print("Cuenta atrás:")
for i in range(5, 0, -1):  # Empieza en 5, para antes del 0, baja de 1 en 1
    print(i)
print("¡Despegue! 🚀")

# Bucle WHILE
# Repetir hasta que se de una condición
respuesta = ""
while respuesta.lower() != "salir":
    respuesta = input("Escribe algo (o 'salir' para terminar): ")

# Se puede usar un bucle FOR para recorrer una lista
invitados = ["Ana", "Juan", "Pedro"]
# Podemos usar el bucle for para recorrer la lista
for nombre in invitados:
    print(f"Bienvenido, {nombre}")