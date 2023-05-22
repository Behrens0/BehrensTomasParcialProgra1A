def aplicarAumento(precio_producto: float)->float:
    """Recibe el precio de un producto y lo devuelve con un aumento del 5 porciento
    
    Args:
        precio_producto(float): Valor Float que se recibe como parametro de precio de un producto
        
    Returns:
        float
    """
    
    precio_producto = precio_producto + precio_producto * 0.05
    return precio_producto

def main():
    aplicarAumento(100)
    
main()