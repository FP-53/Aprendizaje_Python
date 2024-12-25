"""
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""

def anagrama(world_one, world_two):

    if world_one.lower() == world_two.lower():
        return False 
    
    else:
        #sorted ordena todas las letras de la palabra buscando que sean iguales
        return sorted(world_one.lower()) == sorted(world_two.lower())

print(anagrama('Amor', 'Roma'))

print(anagrama('ODIO', 'felicidad'))

print(anagrama('epepeololo', 'ololoepepe'))

