def ordenarCaracteres(cadena_caracteres: str)->str:
    """ordena los caracteres de la cadena pasada por parametro de forma ascendente
    
    Args:
        cadena_caracteres(str): cadena que sera ordenada
        
    Returns: 
        cadena_caracteres(str)
    """
    
    lista_caracteres = list(cadena_caracteres)
    for i in range(len(lista_caracteres) - 1):
        for j in range(i + 1, len(lista_caracteres)):
            if lista_caracteres[i] > lista_caracteres[j]:
                aux = lista_caracteres[i]
                lista_caracteres[i] = lista_caracteres[j]
                lista_caracteres[j] = aux
    cadena_a_devolver = "".join(lista_caracteres)
    return cadena_a_devolver

