# Declaración de funciones
def procesar_retiro(saldo: int, cantidad: int) -> int | None:
    """ PROCESAR RETIROS 
        Args:
            saldo(int): Saldo actual disponible.
            cantidad(int): Cantidad que se desea retirar.
            
        Return:
            int | None: Saldo restante si hay fondos o 'None' si no los hay.
    """
    if cantidad > saldo:
        return None
    else:
        return saldo - cantidad
