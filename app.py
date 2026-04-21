def es_palindromo(texto: str) -> bool:
    """
    Verifica si un texto es palíndromo (ignora espacios y mayúsculas).
    """
    limpio = "".join(c.lower() for c in texto if c.isalnum())
    return limpio == limpio[::-1]

def calcular_descuento(precio: float, porcentaje: float) -> float:
    """
    Calcula el precio final aplicando un descuento.
    """
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100")
    
    return precio * (1 - porcentaje / 100)
