"""
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
"""

def invertir_cadena(texto):
    
    text_len = len(texto) 
    texto_invertido= ""

    for index in range(0,text_len):
        #se usa el -1 para tener en cuenta el ultimo valor del rango que estamos tomando
        texto_invertido += texto[text_len - index -1]

    return texto_invertido

print(invertir_cadena("Hola mundo"))