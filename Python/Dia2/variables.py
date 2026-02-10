# Definición de variables
proyecto = "Analizador de Datos"
horas_estimadas = 20
horas_estimadas2 = "Veinticinco"
precio_hora = 35.5
es_urgente = False
resumen = "El proyecto de hoy se llama " + proyecto + " y explica de forma práctica los tipos de datos y su uso"
nombre = "Francisco"
apellido = "Juan"
nombre_completo = nombre + " " + apellido
edad = 42
ahorros = 550
jubilacion = 67 - edad

# Cálculo automático
coste_total = horas_estimadas * precio_hora
# coste_total = horas_estimadas * precio_hora

# Mostrar resultados
print(f"Proyecto: {proyecto}")
print(f"Coste estimado: {coste_total} euros")
print(f"¿Es urgente?: {es_urgente}")
print(f"Nuevas horas (como texto): {horas_estimadas}")
print(resumen)
print(f"Usuario registrado: {nombre_completo}")
print(f"Te faltan {jubilacion} años para jubilarte y tienes {ahorros} euros")