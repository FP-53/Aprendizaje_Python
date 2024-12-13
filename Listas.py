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
