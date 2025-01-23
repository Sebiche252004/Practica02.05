#areas
import math  

def area_circulo(radio):
    return math.pi * (radio ** 2)

def volumen_cilindro(radio, altura):
    area_base = area_circulo(radio)  
    return area_base * altura

r = input("Introduce el radio del círculo: ")
a = input("Introduce la altura del cilindro: ")

radio = float(r)
altura = float(a)

area = area_circulo(radio)
volumen = volumen_cilindro(radio, altura)

print(f"Área del círculo: {area:.2f}")
print(f"Volumen del cilindro: {volumen:.2f}")
