"""
para escribir hay distintas formas de dar espacios 
    /n= salto de linea
    /t= tabular 

"""


"""
Formatear 
"""
nombre, apellido, edad = "Fidel", "Pizart", 17 

#formas de fomatear
print('Hola, mi nombre es {} {} y mi edad es {}'.format(nombre,apellido,edad))

print('Hola, mi nombre es %s %s y mi edad es %d' %(nombre, apellido, edad))


"""
Para formatear swe usan diversos % segun el tipo de dato 
    %s = strings o cadenas de texto, puede usarse en valores numericos pero no es una buena practica
    %d = valores numericos enteros 
    %f = valores numericos decimales
    "%.number of digits! = valores numericos decimales muy grandes o precisos 


se usa % cuando quieres directamente formatear el valor como texto, se usa .format cuando quieres el valor como tal
se recomienda usar %
"""
#Mejor forma de dar los datos tal como los requieres 
print(f'Hola, mi nombre es {nombre} {apellido} y mi edad es {edad}')

