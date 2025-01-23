#binario

def decimal_a_binario(decimal):
    return bin(decimal)[2:]  

print(decimal_a_binario(25))  

def binario_a_decimal(binario):
    return int(binario, 2)  

print(binario_a_decimal('11001'))  