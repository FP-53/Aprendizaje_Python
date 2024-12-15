"""     LISTAS      """

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

"""Seleccion de varables"""
#se puede seleccionar los valores de una lista para crear variables 
#se colocan en el mismo orden que se encuentra dentro de la lista para que encajen correctamente con cada valor 
#la cantidad de variables deben ser iguales a la cantidad de elementos en la busca o si no debe ser especificado el lugar dentro de la lista

#seleccionar todos los elementos como variable
edad, altura, nombre, apellido = mi_otra_lista
print(nombre)

#seleccionar una variable en especifico dentro de la lista, se puede hacer en mayor cantidad usando , para separar
h = mi_otra_lista[1]
print(h)


"""Concatenar"""
#Concatenar listas 
print(mi_lista + mi_otra_lista)

"""Añadir elementos"""

#.append incerta un nuevo elemento al final de la lista 
mi_otra_lista.append('Perez')
print(mi_otra_lista)

#.insert debes darle el indice, que quieres insertar
mi_otra_lista.insert(3, 'Alejandro') 
print(mi_otra_lista)

"""Eliminar elementos"""

#remueve el elemento que le digas, solo remueve el primer elemento que encuentra con ese nombre
mi_otra_lista.remove(1.76)
print(mi_otra_lista)

#.pop elimina el ultimo elemento de la lista 
mi_otra_lista.pop 
print(mi_otra_lista)
#si vuelves a imprimir el .pop te da el valor que quito 
print(mi_otra_lista.pop())
#puedes hacer pop a un elemento en concreto dentro de la lista usando () 

#puedes usar pop para crear variables 
elemento_pop = mi_otra_lista.pop()
print(elemento_pop)

#pop puede usarse para mover elementos entre listas usando variables 
print(mi_lista)
mi_lista.append(elemento_pop)
print(mi_lista)

mi_otra_lista.append('Pizart')
mi_otra_lista.append('Perez')

"""Otras formas de eliminar: 
    del= elimina un elemento segun el indice 
    clean= borra la lista
"""

"""Cambiar valores"""

mi_otra_lista[0] = 18
print(mi_otra_lista)

"""Copiar una lista"""

mi_nueva_lista = mi_otra_lista.copy()
print(mi_nueva_lista)


"""Girar la lista"""
mi_nueva_lista.reverse()
print(mi_nueva_lista)

"""Ordenar la lista"""
#ordena por defecto en orden alfabetico o numerico segun la lista
mi_nueva_lista.sort()
print(mi_nueva_lista)

