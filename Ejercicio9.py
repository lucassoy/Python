class Estudiante:
    def __init__(self,name,age,notas):
        self.name = name
        self.age = age
        self.notas = notas
    def promedio(self):
        return sum(self.notas)/len(self.notas)
e1 = Estudiante("Lucas", 20, [90, 80, 85])
e2 = Estudiante("Juan", 21, [100, 90, 95])
for e in [e1, e2]:
    print(e.name, e.age, e.notas)
    print("Promedio:", e.promedio())