"""     DICCIONARIOS        """

#formas de llamar un diccionario 
my_dict = dict( )

#los valores de un diccionarios van relacionados en pares 
my_other_dict = { 'Nombre':'Fidel', 'Apellido':'Pizart', 'Edad':17, 1:'Python'}

my_dict={
    'Nombre': 'Alejandro',
    'Apellido': 'Perez',
    'Edad': 71,
    #Se pueden guardar sets como valores de un diccionario 
    "Lenguajes de programacion": {'HTML', 'CSS', 'Pyton'}, #Aunque contenga varios elementos en el set, aun asi cuenta como un solo elemento 
    1:1.77
}
#Los diccionarios asocian una clave a un valor

print (my_dict)
print (len(my_dict))

#No se usan indices, para buscar un valor la clave funciona como si fuera un indice 
print(my_dict['Lenguajes de programacion'])

#actualizar un valor
my_dict['Nombre'] = 'Fidel'
print(my_dict['Nombre'])

#añadir un valor 
my_dict['Pais'] = 'Panama'
print(my_dict)

#eliminar algo dentro del diccionario
del my_dict['Pais']
print (my_dict)

#Para buscar un valor necesitamos buscar dentro de la clave 
print( 'Fidel' in my_dict) #esto es un error
print( 'Fidel' in my_dict['Nombre']) #esto es la forma correcta de buscar un valor, buscarlo dentro de la clave 


print( 'HTML' in my_dict['Lenguajes de programacion'] ) #funciona aun cuando lo buscas dentro de un set 

# .items muestra todas las claves con sus valores 
print(my_dict.items())

# .keys te da un listado de las claves
print(my_dict.keys())

# .values te da un listado de los valores
print(my_dict.values())

# muestra diccionario sin los valores 
print(my_dict.fromkeys(('Nombre', 1)))

#EJEMPLO DE USO .fromkeys

my_new_dict = my_dict.fromkeys(('Nombre', 'Apellido'))
print(my_new_dict)

"""
.Fromkeys normalmente no es muy bueno usarlo, su mejor uso es para crear un diccionario sin valores, tiene muy pocos usos
Tambien se usa para transformas listas a diccionarios
"""

#de lista a diccionario 

my_list = ['Nombre', 'Edad', 'Apellido']
print(type(my_list))
my_newnew_dict= dict.fromkeys(my_list)
print(my_newnew_dict)
print(type(my_newnew_dict))

"""
El mayor uso de .fromkeys es crear un nuevo diccionario en base a otro, con las mismas claves pero sin los valores 
"""

"""MANTENER VALORES"""

dict_prueba = { 'Nombre': 'Fidel', 'Apellido': 'Pizart', 'Edad': 17, 'Pais':'Panama'}
print(dict_prueba)
dict_prueba2 = dict.fromkeys(dict_prueba, ('Fidel', 'Pizart')) #??? error, todos los valores van a ser esos 
print(dict_prueba2)
dict_prueba2 = dict.fromkeys(dict_prueba, 'F') #no es posible mantener un valor, se puede asignar valores a TODAS las claves pero no a una o algunas en especifico
print(dict_prueba2)