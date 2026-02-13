# --- DECLARACIÓN DE VARIABLES ---
lista_invitados = []
nuevo_invitado = ""
dic_invitados = {}

# --- LÓGICA DEL SCRIPT ---
while nuevo_invitado.lower() != "nadie":
    nuevo_invitado = input("Escribe el nombre de un nuevo invitado:")
    if len(nuevo_invitado) > 2 and nuevo_invitado.lower() != "nadie":
        edad = int(input(f"Cuál es su edad? "))
        dic_invitados = {
            "nombre": nuevo_invitado,
            "edad": edad
            }
        lista_invitados.append(dic_invitados)
    elif len(nuevo_invitado) < 3:
        print("Nombre demasiado corto")

# --- IMPRESIÓN DE LA LISTA DE INVITADOS ---
for dic_invitados in lista_invitados:
    nombre = dic_invitados["nombre"]
    edad = dic_invitados["edad"]
    print(f"Invitado: {nombre} -Edad: {edad}")
