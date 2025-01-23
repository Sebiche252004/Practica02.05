#factorial
def factorial_iterativo(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)
numero = 9
print(f"Factorial (iterativo) de {numero}: {factorial_iterativo(numero)}")
print(f"Factorial (recursivo) de {numero}: {factorial_recursivo(numero)}")
