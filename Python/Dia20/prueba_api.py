import requests

url = "https://api.exchangerate-api.com/v4/latest/EUR"

try:
    respuesta = requests.get(url, timeout=5) # Ponemos un tiempo límite de 5 seg por si internet va lento
    
    # Esta línea lanza un error automáticamente si el código no es 200
    respuesta.raise_for_status() 
    
    datos = respuesta.json()
    moneda = input("¿Qué moneda quieres consultar?(introduce el código de la moneda como GBP, USD, JPY, ETC.)").upper()
    precio = datos["rates"].get(moneda)

    if precio:
        print(f"El cambio de {moneda} es: {precio}€")
    else:
        print(f"❌ La moneda '{moneda}' no está disponible.")

except requests.exceptions.HTTPError as err:
    print(f"❌ Error de HTTP: {err}")
except requests.exceptions.ConnectionError:
    print("❌ Error: No tienes conexión a internet.")
except Exception as e:
    print(f"❌ Ocurrió un error inesperado: {e}")