import json

def cargar_datos():
    # Usamos global para avisar que vamos a llenar los diccionarios de fuera
    global biblioteca, usuarios 
    
    try:
        with open("biblioteca.json", "r") as archivo:
            datos = json.load(archivo)
            
            # --- PASO 1: Reconstruir Usuarios ---
            for id_s, d in datos["usuarios"].items():
                nuevo_usuario = Usuario(d["id_socio"], d["nombre"])
                usuarios[id_s] = nuevo_usuario
                # Nota: Dejamos la lista de libros_en_mano vacía por ahora
            
            # --- PASO 2: Reconstruir Libros ---
            for isbn, d in datos["libros"].items():
                nuevo_libro = Libro(d["isbn"], d["titulo"], d["autor"])
                
                # ¿Tenía este libro un usuario asignado?
                id_user = d["usuario_actual"]
                if id_user:
                    # Buscamos el objeto Usuario que ya creamos en el Paso 1
                    objeto_usuario = usuarios[id_user]
                    
                    # Conectamos ambos cables:
                    nuevo_libro.usuario_actual = objeto_usuario # El libro apunta al usuario
                    objeto_usuario.libros_en_mano.append(nuevo_libro) # El usuario apunta al libro
                
                biblioteca[isbn] = nuevo_libro
                
        print(">>> Memoria recuperada con éxito.")

    except FileNotFoundError:
        print("No se encontró archivo de datos. Iniciando biblioteca vacía.")