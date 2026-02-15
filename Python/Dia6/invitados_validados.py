# --- FUNCION ---
def validar_nombre(nombre: str, n_caracteres: int = 3) -> bool:
    """Valida que elnombre tenga almenos3 caracteres.

    Args:
        nombre (str): Nombre de la persona a validar.
        n_caracteres (int): caracteres minimos a validar (3 por defecto)
        
    Returns:
        bool: el nombre tiene al menos X caracteres True/False
    """
    if len(nombre) < n_caracteres:
        return False
    else:
        return True

# --- DECLARACIÓN DE VARIABLES ---
lista_invitados = []
nuevo_invitado = ""
dic_invitados = {}

# --- LÓGICA DEL SCRIPT ---
while nuevo_invitado.lower() != "nadie":
    nuevo_invitado = input("Escribe el nombre de un nuevo invitado:")
    if validar_nombre(nuevo_invitado) == True and nuevo_invitado.lower() != "nadie":
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
