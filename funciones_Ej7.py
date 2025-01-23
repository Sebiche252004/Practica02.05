def contar_palabras(texto):
    palabras = texto.lower().split()  
    frecuencia = {}
    for palabra in palabras:
        palabra = palabra.strip(".,;:!¡¿?\"'()")  
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

texto = "Tres tristes tigres comian trigo en un trigal, el trigo en el trigal y los tigres tristes"
frecuencias = contar_palabras(texto)
print(frecuencias)  

def palabra_mas_repetida(diccionario):
    if not diccionario:
        return None  
    palabra_max = max(diccionario, key=diccionario.get)
    return palabra_max, diccionario[palabra_max]


mas_repetida = palabra_mas_repetida(frecuencias)
print(mas_repetida) 
