# media
def calcular_media(lista_numeros): 
    if len(lista_numeros) == 0:
        return "No se encuentran valores dentro de la lista"
    
    suma = sum(lista_numeros)  
    cantidad = len(lista_numeros)  
    media = suma / cantidad 
    return media  

numeros = [6, 7, 10, 25, 30]

media = calcular_media(numeros)

print(f"La media de los números es de: {media}")
