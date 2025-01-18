print("dime un numero a multiplicar")
numero = int(input())
if(numero <1 or numero >10):
    print("El numero debe estar entre 1 y 10")
    exit()
else:
    for i in range(1, 11):
        print(numero, "*", i, "=", numero * i)