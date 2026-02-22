def venta(diccionario: dict, nombre: str, cantidad: int) -> bool | int:
    """
    Procesa la venta y descuenta el stock
    Return: devuelve es stock restanto o False en caso de que no se pueda hacer la venta
    Atención: En case de devolver un stock de '0', las funciones lógicas pueden entenderlo como venta fallida.
    """
    if cantidad <=0:
        return False
    if diccionario.get(nombre) is None:
        return False
    if diccionario[nombre]["stock"] >= cantidad:
        diccionario[nombre]["stock"] -= cantidad
        return diccionario[nombre]["stock"]
    else:
        return False

def n_categoria(categorias: set, nueva: str):
    """
    Añade una categoría de producto.
    """
    categorias.add(nueva.lower())

def valor_stock(diccionario: dict) -> float:
    """
    Genera el total del valor del stock restante
    """
    val_stock: float = 0
    for a in diccionario.values():
        val_stock = val_stock + (a["precio"] * a["stock"])
    return val_stock

