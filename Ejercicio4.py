import random

random_number = random.randint(1, 100)
intento = 0
numero = 0
while (numero != random_number and intento < 5):
    print("Dime un numero entre 1 y 100")
    numero = int(input())
    if(numero < 1 or numero > 100):
        print("El numero debe estar entre 1 y 100")
        exit()
    else:
        if(numero < random_number):
            print("El numero es mayor")
        elif(numero > random_number):
            print("El numero es menor")
        else:
            print(" Has acertado!")
            break
        intento += 1
if numero != random_number:
    print("Has perdido, el numero era", random_number)