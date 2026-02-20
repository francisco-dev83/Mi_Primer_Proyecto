productos = [
    {"nombre": "ratón", "precio": 25},
    {"nombre": "teclado", "precio": 50},
    {"nombre": "monitor", "precio": 150},
    {"nombre": "cable hdmi", "precio": 8},
    {"nombre": "alfombrilla", "precio": 12}
]

catalogo_premium = [f"Producto: {p["nombre"].upper()} - Precio: {p["precio"]}€" for p in productos if p["precio"] > 20]
print(catalogo_premium)
