def calcular_iva(precio: float, impuesto: float = 21.0) -> float:
    """Calcula el precio final con IVA incluido.

    Args:
        precio (float): El precio base del producto.
        impuesto (float): El porcentaje de IVA (por defecto 21.0).

    Returns:
        float: El precio total con el impuesto aplicado.
    """
    total = precio * (1 + impuesto / 100)
    return total

# PRUEBA: Si pasas el ratón por encima de 'calcular_iva' aquí abajo, 
# verás la magia de la ayuda flotante en VS Code.
resultado = calcular_iva(100)
print(f"Total: {resultado}")