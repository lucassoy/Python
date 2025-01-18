lista = []
numero = 0
for i in range(5):
    print("Dime un numero de la lista")
    numero = int(input())
    lista.append(numero)
print("")
for i in range(5):
    print(lista[i])

print("El numero mas grande de la lista es:", max(lista))
print("El numero mas pequeño de la lista es:", min(lista))
print("El promedio de la lista es:", sum(lista) /5)
print("Ahora vamos a ordenarlos:")
for i in range(5):
    for j in range(5):
        if lista[i] < lista[j]:
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp
print("")
print("El orden correcto es:",lista)