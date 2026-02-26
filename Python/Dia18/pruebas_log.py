from datetime import datetime

# Obtenemos la fecha y hora exacta de ahora
ahora = datetime.now()
fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M:%S")

with open("historial.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"[{fecha_formateada}] Se ha registrado una actividad\n")