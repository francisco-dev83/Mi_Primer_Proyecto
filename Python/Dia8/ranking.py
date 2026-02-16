# Generación de lalista
puntuaciones: list[int] = [45, 82, 10, 95, 55, 67]

# Ejercicios
puntuaciones.sort(reverse=True)
top_tres: list[int] = puntuaciones[0:3]
colistas: list[int] = puntuaciones[-2:]
print("PODIO")
for i, nota in enumerate(top_tres, start=1):
    print(f"Puesto {i}- {nota}")
print("COLISTAS")
for i, nota in enumerate(colistas, start=1):
    print(f"Puesto {i}- {nota}")
