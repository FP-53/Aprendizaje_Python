"""
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""

def es_primo():
    for numero in range(0,101):
        is_divisible=True
        if numero>=2: 
            is_divisible = False
            for index in range(2,numero):
                if numero%index == 0:
                    is_divisible= True
                    break
        
        if not is_divisible:
            print(numero)

es_primo()