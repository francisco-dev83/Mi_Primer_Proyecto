import json
import os # Para comprobar si el archivo existe
from datetime import datetime

class GestorInventario:
    def __init__(self):
        self.archivo = "inventario.json"
        self.cargar_datos() # Intentamos cargar al iniciar
    
    def cargar_datos(self):
        if os.path.exists(self.archivo):
            print(f"Buscando el archivo en: {os.path.abspath(self.archivo)}")
            with open(self.archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                self._productos = datos["productos"]
                # JSON no guarda SETS, así que lo convertimos de vuelta
                self._categorias = set(datos["categorias"])
        else:
            # Datos por defecto si el archivo no existe
            self._productos = {
                "monitor": {"precio": 150.0, "stock": 10},
                "raton": {"precio": 25.0, "stock": 45}
            }
            self._categorias = {"periféricos", "imagen"}
    
    def guardar_datos(self):
        datos_a_guardar = {
            "productos": self._productos,
            "categorias": list(self._categorias) # El puente que planeamos ayer
        }
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos_a_guardar, f, indent=4, ensure_ascii=False)
        print("💾 Datos guardados correctamente.")
    
    def registrar_log(self, mensaje: str):
        ahora = datetime.now()
        fecha = ahora.strftime("%d/%m/%Y %H:%M:%S")
        with open("ventas.log", "a", encoding="utf-8") as archivo:
            archivo.write(f"[{fecha}] {mensaje}\n")

    def vender(self, nombre: str, cantidad: int) -> bool:
        if cantidad <=0:
            return False
        if self._productos.get(nombre) is None:
            return False
        if self._productos[nombre]["stock"] >= cantidad:
            self._productos[nombre]["stock"] -= cantidad
            return self._productos[nombre]["stock"]
        else:
            return False

    def calcular_total(self) -> float:
        val_stock: float = 0
        for a in self._productos.values():
            val_stock = val_stock + (a["precio"] * a["stock"])
        return val_stock
    
    def n_categoria(self, nueva: str):
        self._categorias.add(nueva.lower())