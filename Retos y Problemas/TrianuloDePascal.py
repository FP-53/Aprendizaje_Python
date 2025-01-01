def pascal_tri(numFilas):
    '''Imprime el triángulo de Pascal con numFilas.'''
    for i in range(numFilas):
        print(''*(numFilas-i), end='')
        # calcular la potencia de 11
        print(' '.join(str(11**i)))

pascal_tri(5)

