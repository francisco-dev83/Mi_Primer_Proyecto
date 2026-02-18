# declaración del diccionario
jugador: dict[str, any] = {
    "nombre" : "Pepe",
    "nivel" : 1,
    "habilidades" : ["Fuego", "Agua", "Salto"],
    "equipo" : {
        "arma" : "espada",
        "escudo" : "escudo de madera"
    }
}

# declaración de variables
nom_jugador = jugador["nombre"]
arma_jugador = jugador["equipo"]["arma"]
hab_jugador = ", ".join(jugador["habilidades"])
inv_pociones = jugador.get("pociones", "El inventario de pociones está vacío")

# Salida de información
print(f"El jugador {nom_jugador} lleva una {arma_jugador} y tiene éstas habilidades: {hab_jugador}")
print(inv_pociones)