# 1. Entrada de datos
nombre = input("¿Cómo te llamas? ")
edad_texto = int(input("¿Cuántos años tienes? "))

# 2. El Casting (Conversión de texto a número entero)
# edad_numero = int(edad_texto)

# 3. Operación
# edad_perro = edad_numero * 7
edad_perro = edad_texto * 7

# 4. Salida interactiva
print(f"Hola {nombre}, si fueras un perro tendrías {edad_perro} años.")