def reemplazar_prodcutos(cadena_cartacteres: str, caracter: str, segundo_caracter: str)->int:
    """ reemplaza cada ocurrencia del segundo parámetro por el tercero en la cadena de caracteres pasado por parametro
    
    Args:
        cadena_caracteres(str): cadena que sera modificada por los caracteres
        caracter(str): caracter que sera reemplazado de la cadena
        segundo_caracter(str): caracter que sera colocado en lugar del primer caracter
        
    Returns:
        cantidad_reemplazos(int)
    
    """
    
    cadena_caracteres = cadena_cartacteres.replace(caracter, segundo_caracter)
    cantidad_reemplazos = cadena_cartacteres.count(caracter)
    return cantidad_reemplazos
    
