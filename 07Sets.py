"""     Sets        """

my_set = set()
print(type(my_set))

# las llaves {} se usan para crear diccionarios y sets, por defecto te da tipo diccionario
my_other_set = {}
print(type(my_other_set))

my_other_set = {'Fidel', 'Pizart', 17, 1.76}
print(type(my_other_set))

""" 
UN SET ES UNAS LISTA DESORDENADA, NO IMPORTA EL ORDEN EN QUE AÑADAS LOS VALORES
- Se usan las mismas funciones que en una lista
- No admite repetidos 
"""

print(my_other_set)

# No se puede acceder a un punto en concreto del set
# print(my_other_set[2])

"""Comprobar si un elemento existe dentro del set"""

# 'Fidel' existe en my_other set?
print('Fidel' in my_other_set)

print('Alejandro' in my_other_set)