class GestorInventario:
    def __init__(self):
        self._productos = {
            "monitor": {"precio": 150.0, "stock": 10},
            "raton": {"precio": 25.0, "stock": 45},
            "teclado": {"precio": 50.0, "stock": 30}
        }
        self._categorias = {"periféricos", "imagen"}
        

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