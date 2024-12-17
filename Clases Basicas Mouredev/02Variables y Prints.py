
"""
Tipos de Variable y pruebas de inputs 
"""



#Variable tipo cadena de texto
user_name= input('Como te llamas?')
print(user_name)

#variable numerica
numero_de_usuario = input('Que edad tienes?')
print ('Numero de usuario', numero_de_usuario)

#variable boleana
mayor_de_edad = False
print('Es mayor de edad?', mayor_de_edad)


"""
Print y algunas de sus funciones 
"""

#str=vonvierte datos en cadenas de texto
int_to_str_variable = str(numero_de_usuario)
print(int_to_str_variable)

#type= ta da el tipo de variable que tienes
print(type(int_to_str_variable))

print(user_name, str(numero_de_usuario), mayor_de_edad)

"""
Print no te pide un tipo de dato en especial, funciona con todos los tipos de datos
"""

#len te da la cantidad de caracteres de la variable, los espacios entre palabras se cuentan
print(len(user_name))


#Un input puede sobre escribir un valor que ya habias definido antes
pais = 'Cuba'
print(pais)

pais= input('En que pais vives?')
print(pais)