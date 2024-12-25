"""
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
"""

def fibonacci():
    fibonacci_list = [0,]

    first_number= 0

    second_number=1 

    while len(fibonacci_list)<=50: 
        new_number= first_number + second_number
        first_number=second_number
        second_number=new_number

        fibonacci_list.append(new_number)

    print(fibonacci_list)

fibonacci()

