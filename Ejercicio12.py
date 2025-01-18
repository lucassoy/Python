class libro:
    def __init__(self, name):
        self.name = name

class Estudiante:
    def __init__(self,name,libro):
        self.name = name
        self.libro = libro
class Prestamo:
    def __init__(self,estudiante,libro):
        self.estudiante = estudiante
        self.libro = libro

l1 = libro("Python")
l2 = libro("Java")
e1 = Estudiante("Lucas", l1)
e2 = Estudiante("Juan", l2)
p1 = Prestamo(e1, l1)
p2 = Prestamo(e2, l2)
for p in [p1, p2]:
    print(p.estudiante.name, p.libro.name)