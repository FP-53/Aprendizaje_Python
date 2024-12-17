"""     FUNCIONES       """

"""
Una funcion intenta resolver un problema en concreto dentro del codigo, evita tener que duplicar codigo si no que debes llamar a la funcion
"""
#def es la palabra reservada para crear funciones
def my_function(): 
    print('esto es una funcion')
#una funcion es una seccion de codigo que podemos llamar para que se repita, puede ser tan copmpleja como el codigo q   ue contenga 

#llamamos a la funcion'
my_function()
#asi de simple se llama a una funcion 

""" JAMAS LLAMAR UNA FUNCION DENTRO DE SI MISMA, LA COMPUTADORA EXPOTA"""

#se le pueden asignqar valores a la funcion que son necesarios para que funcione 
def sum_two_values (value1:int, value2:int):
    print(int(value1) + int(value2))

value1 = input('Dime un numero para sumar')
value2 = input('Dime un numero para sumar')


#value1 y value2 son los parametros que necesita para poder realizar la funcion
sum_two_values(value1, value2)

"""RETORNAR DATOS"""
def sum_two_values_retorn (value1:int, value2:int):\
    #return funciona para dar el valor que puedes almacenar en una variable, sin return el valor que se guarde en las variables sera None
    return value1 + value2

my_result = sum_two_values_retorn(5,5)

print(my_result)

def print_name (name, surname):
    print(f'{name} {surname} ')

#Se puede modificar el orden
print_name(surname='Pizart',name='Fidel')

#Valores default, puedes asignar valores por defecto y asi esos valores no son necesarios al momento de iniciar la funcion
def print_name_default (name, surname, alias = 'Sin alias'):
    print(f'{name} {surname} {alias}')


print_name_default('Fidel', 'Pizart')

#usar asterisco delante de el nombre del parametro, se puede usar varias formas de ese parametro 
def print_texts(*text):
    print(text)


print_texts('Hola', 'Python', 'Fide')


#imprimir los valores por separado
def print_upper_texts(*texts):
    for text in texts: 
        print(text.upper())

print_upper_texts('hola', 'adios', 'buenos dias')

