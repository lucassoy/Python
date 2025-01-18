empleados = {
    1: {"nombre": "Juan", "salario": 50000},
}

print(empleados)
empleados[2] = {"nombre": "Lucas", "salario": 60000}
# Cambiar el nombre de Juan a Jorge
empleados[1]["nombre"] = "Jorge"
print(empleados)

# Eliminar el empleado con id 2
empleados.pop(2)
print(empleados)