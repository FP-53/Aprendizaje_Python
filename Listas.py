### LISTAS ###

mi_lista = list() #mo me gusta usarlo pq causa mas errores que si usara []

mi_otra_lista = []

#dos formas de crear o marcar una lista, perfiero []


print(len(mi_lista))

mi_lista = [35, 17, 24, 62, 52, 30, 30, 18]

print(mi_lista)
print(len(mi_lista))
#en las listas 'len' muestra la cantidad de elementos que conforman la lista\

mi_otra_lista = [17, 1.76, 'Fidel', 'Pizart']

print(mi_otra_lista)
#una lsita puede contener mas de un tipo de datos 

print(type(mi_otra_lista))
#todas las listas tienen como type 'class list' 



"""Acceder a elementos por separado en una lista"""

print(mi_otra_lista[0])
# para seleccionar un valor en concreto se coloca 'nombre de la lista[numero del elemento]', el primer elemento de una lista siempre es el 0, el segundo es el 1 y asi 

print(mi_otra_lista[0])
print(mi_otra_lista[1])

#los numeros negativos cuentan desde el ultimo al primero empezando por -1
print(mi_otra_lista[-1])
print(mi_otra_lista[-3])

#si el numero no es posible buscarlo pq dicho numero no esta en la lista, causa IndexError 
#ejemplo print(mi_otra_lista[5])

#colocar nombre_de_lista.count(x) te dira cuantos elementos iguales existen de el valor que coloques entra los parentesis 
print(mi_otra_lista.count('Fidel'))
print(mi_lista.count(30))


#se puede seleccionar los valores de una lista para crear variables 
#se colocan en el mismo orden que se encuentra dentro de la lista para que encajen correctamente con cada valor 
edad, altura, nombre, apellido = mi_otra_lista
print(nombre)

