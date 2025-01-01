### FUNCIONES DE ORDEN SUPERIOR ###

#son funciones que usan otras funciones que ya existen


def sum_one(value):
    return value + 1 

def sum_two_values_and_add_one(fisrst_value, second_value, f):
    return f(fisrst_value + second_value)
#usas f para llamar a la funcion anterior, se puede usar con objetos o usos mucho mas copmplejos

print(sum_two_values_and_add_one(5, 2, sum_one))

#llamamos una funion dentro de otra funcion \

# Closures 
#las closures son funciones que returnan otras funciones
def add_ten():
    #defines una funcion dentro de una funcion
    def add (value):
        return value + 10
    
    #retornas una nueva funcion dentro de la misma funcion
    return add

#esta variable contiene una funcion
add_closure = add_ten()

print(add_closure(5))


#Map

values = [2, 5, 11, 15 ]

def duplicate(value):
    return value*2

print(list(map(duplicate, values)))

#un map itera sobre cada valor iterable usando la funcion, por cada objeto de la lista usa la funcion '

#usar una lambda en vez de una una fucion es mejor en este caso 
print(list(map(lambda number: number * 2, values)))

#Filter 

def filter_greater_ten(number):
    if number>10: 
        return True
    else:
        return False


#filter necesita valores boleanos que analizar los valores de la variable que le des y devolver los que sean verdaderos 

print(list(filter(filter_greater_ten,values)))
print(list(filter(lambda values: values > 10,values)))