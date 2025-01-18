def factorizar(numero):
    if numero < 0:
        return "No se puede factorizar un numero negativo"
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

print("Dime un numero que quieras factorizar")
numero = int(input())
resultado = factorizar(numero)
print("El factorial de", numero, "es", resultado)