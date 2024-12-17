my_list = [30, 40, 60, 15, 17, 54]
print('LISTA')
for element in my_list:
    print(element)

print('TUPLE')
my_tuple = (35, 17, 'Fidel', 'Pizart')
for element in my_tuple:
    print(element)

print('DICCIONARIO')
my_other_dict = { 'Nombre':'Fidel', 'Apellido':'Pizart', 'Edad':17, 1:'Python'}
for element in my_other_dict.values():
    print(element)
else:
    print('el bucle termino')

