# Tuple y Set
# Declaración de listas
lista_negra: tuple[str] = ("Roberto Estévez", "Claudio Vip", "Marta Malas")
registro_entrada: list[str] = ["Francisco", "Ana López", "Marcos Ruíz", "Francisco", "Lucía Sanz", "Ana López", "Roberto Estévez", "Marcos Ruíz"]

# Lógica del código
entrada_limpia = set(registro_entrada)
negra_set = set(lista_negra)

invitados_ok = entrada_limpia - negra_set


# Mostrar datos
print("Listade invitados válidos")
for nombre in invitados_ok:
    print(nombre)