usuarios_sucios = ["  juan", "anA  ", "  PePe", "marta "]

usuarios_limpios = [ul.strip().capitalize() for ul in usuarios_sucios if len(ul.strip()) > 3]
print(usuarios_limpios)