"""     Excepciones     """

#try y exception se usan para evitar erroes que puedan romper o dañar la aplicacion o el proceso
number1 = 5

number2 = '1'

#el codigo se rompe por tener dos valores de distintos tipos, un entero y una cadena de texto 
#print(numer1 + number2)

#try execpt
try:
    print(number1 + number2)
    print('Funciona correctamentye')
except:
    print('Se ha cometido un error')


#try except else
try:
    print(number1 + number2)
    print('No se ha producido un error')
except:
    print('Se ha cometido un error')
else:
    #else va a funcionar si el camino anterior no funciona, si el except no se activa el else se activa 
    print('La ejecucion continua correctamente')

#try except else finally
try:
    print(number1 + number2)
    print('No se ha producido un error')
except:
    #se ejecuta si try falla 
    print('Se ha cometido un error')
else:
    #else va a funcionar si el camino anterior no funciona, si el except no se activa el else se activa 
    print('La ejecucion continua correctamente')
finally:
    #se ejecuta siempre al final 
    print('La ejecucion continua')


#Excepciones por tipo
try:
    print(number1 + number2)
    print('No se ha producido un error')
except TypeError as error:
    #se ejecuta solo con ese tipo de error que elijes
    print('Hay un error')
    print(error)