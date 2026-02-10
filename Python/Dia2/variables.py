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
a = 500
b = 500
frase = "Python es genial"
puntuación = 0.085743
variable_inicial = " hola mundo "
variable_final = variable_inicial.strip()

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
print(f"valor de a: {a} - ID en memoria: {id(a)}")
print(f"Valor de b: {b} - ID en memoria: {id(b)}")
print(f"¿Son el mismo objeto?: {a is b}")
a = a + 1
print("Sumemos 1 en a")
print(f"valor de a: {a} - ID en memoria: {id(a)}")
print(f"Valor de b: {b} - ID en memoria: {id(b)}")
print(f"¿Son el mismo objeto?: {a is b}")
print(frase.upper())
print(frase.title())
print(frase.replace("genial", "increíble"))
print(frase)
print(f"Tu puntuación es {puntuación:.2%}")
print(f"La frase inicial es: {variable_inicial}")
print(f"La frase limpia es: {variable_final}")
print(f"La frase limpia tiene {len(variable_final)} caracteres")