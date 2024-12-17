"""     CONDICIONALES y BUCLES       """

print("vamos a adivinar tu numero")
my_value = int(input("Dime un numero POSITIVO:"))


if my_value%2==1: 
    print('tu numero es impar')
else:
    print('tu numero es par')


if my_value>100:
    print('Tu numero es mayor que 100')
    type_number= 1

if my_value<100:
    print('Tu numero es menor que 100')
    type_number= -1

if my_value == 100: 
    print('Tu numero es 100')


"""
Tipos de bucles
- While: necesita una condicion que se cumpla para funcionar, se repite mientras se cumpla esa funcion
- For: itera mas de un elemento en una lista, itera 1 vez por cada elemento de la lista y en cada uno de ellos
- 
"""
diference=0


while my_value>100:
        
        #SI EL NUMERO ES MAYOR QUE 100
        if type_number== 1 and my_value>100:
            my_value-= 1
            diference-=1
        else: 
            if type_number== 1 and my_value>110:
                my_value-= 10
                diference-=10
            else:
                if type_number== 1 and my_value>200:
                    my_value-= 100
                    diference-=100
                else:
                    if type_number== 1 and my_value>1000:
                        my_value-= 1000
                        diference-=1000
                    else:   
                        if type_number== 1 and my_value>10000:
                            my_value-= 10000
                            diference-=10000
                        else:
                            if type_number== 1 and my_value>100000:
                                my_value-= 100000
                                diference-=100000

while my_value<100:
        #SI EL NUMERO ES MENOR QUE 100
        if type_number== -1 and my_value<100:
            my_value+=1
            diference+=1
        else:
            if type_number== -1 and my_value<110:
                my_value+= 10
                diference+=10
            else:
                if type_number== -1 and my_value<110:
                    my_value+= 10
                    diference+=10
                else:
                    if type_number== -1 and my_value<110:
                        my_value+= 10
                        diference+=10
                    else: 
                        if type_number== -1 and my_value<200:
                            my_value+= 100
                            diference+=100
                        else:
                            if type_number== -1 and my_value<1000:
                                my_value+= 1000
                                diference+=1000
                            else:
                                if type_number== -1 and my_value<10000:
                                    my_value+= 10000
                                    diference+=10000
                                else:
                                    if type_number== -1 and my_value<10000:
                                        my_value+= 10000
                                        diference+=10000

if diference>100:
        real_number = 100 + diference 
else:
        real_number = 100 - diference 

print('Tu numero es: ', real_number)