from random import randint
numeros = []
def sorteio(numeros):
    for v in range(0, 5):
        numeros.append(randint(0,10))
    print('Sorteando 5 valores da lista: ',end = '')
    for c in numeros:
        print(f'{c}', end = ' ')
    print()

def somaPar(numeros):
    s = 0
    for v in numeros:
        if v % 2 == 0:
            s += v
    print(f'Somado os valores pares de {numeros} temos {s}')

sorteio(numeros)
somaPar(numeros)




