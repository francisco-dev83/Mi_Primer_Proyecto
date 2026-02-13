# --- DECLARACIÓN DE VARIABLES ---
lista_invitados = []
nuevo_invitado = ""

# --- LÓGICA DEL SCRIPT ---
while nuevo_invitado.lower() != "nadie":
    nuevo_invitado = input("Escribe el nombre de un nuevo invitado:")
    if len(nuevo_invitado) > 2 and nuevo_invitado.lower() != "nadie":
        lista_invitados.append(nuevo_invitado)
    elif len(nuevo_invitado) < 3:
        print("Nombre demasiado corto")

# --- IMPRESIÓN DE LA LISTA DE INVITADOS ---
for nombre in lista_invitados:
    print (nombre)
