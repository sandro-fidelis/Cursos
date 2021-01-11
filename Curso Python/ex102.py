def fatorial(n=1, show=True):
    """
    -> Mostra o fatorial escilhido pelo usuário.
    :param n: Valor escolhido para mostrar o fatorial
    :param show: (Opcional) Mostra ou não a sequência de valores até o resultado
    :return: sem retorno
    """
    c = n
    if show == True:
        while c >= 2:
            print(f'{c} X', end=' ')
            c -= 1
            if c == 1:
                print('1 =', end=' ')

    f = 1
    for c in range(n, 0, -1):
        f *= c
    print(f)


# PROGRAMA PRINCIPAL
n = int(input('Digite um numero para ver seu fatorial: '))
fatorial(n, show = True)


#GUANABARA


def fatorial(n, show = True):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show:(OPCIONAL) Mostrar ou nõa a conta.
    :return: O valor do Fatorial de um número (n)
    """
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            print(c, end = '')
            if c > 1:
                print(' X ', end = '')
            else:
                print(' = ', end='')
        f *= c
    return f

help(fatorial)
print(fatorial(5, show = True))