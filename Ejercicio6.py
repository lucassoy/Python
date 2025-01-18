def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
print("dime un numero y te diré si es primo o no")
numero = int(input())
es = False
es = es_primo(numero)
if es:
    print("El número es primo")
else:
    print("El número no es primo")