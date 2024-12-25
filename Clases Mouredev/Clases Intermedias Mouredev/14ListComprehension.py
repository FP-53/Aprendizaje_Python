### LIST COMPREHENSION ### 

my_original_list= [0,1,2,3,4,5,6,7,8,9]
print(my_original_list)

#las listas de comprension se usan para traer elementos de varias listas a una sola lista
#es una forma mas rapida de hacer listas, tenemos lo mismo pero mas rapido y eficiente
my_list = [i for i in range(10)]
#usamos un rango para hacer ejemplo, pero se puede usar una lista aparte para 
print(my_list)

#va a sumar 1 a cada valor de la lista
my_list = [i + 1 for i in range(10)]
print(my_list)

#va a duplicar cada valor de  la lista
my_list = [i * 2 for i in range(10)]
print(my_list) 

my_list = [i * i for i in range(10)]
print(my_list)

#ejemplo de uso 

def sum_five(num):
    return num + 5

my_list = [sum_five(i) for i in range(10)]
print(my_list)
