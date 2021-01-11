def moeda(p = 0, moeda = 'R$'):
    return f'{moeda} {p:.2f}'.replace('.',',')


def metade(p=0, show = True):
    r = p / 2
    if show == True:
        return moeda(r)
    else:
        return r


def dobro(p=0, show = True):
    r = p * 2
    if show == True:
        return moeda(r)
    else:
        return r

def aumentar(p=0, taxa=0, show = True):
    r = p + ((p * taxa) / 100)
    if show == True:
        return moeda(r)
    else:
        return r

def diminuir(p, taxa, show = True):
    r = p - ((p * taxa) / 100)
    if show == True:
        return moeda(r)
    else:
        return r

def resumo(p,taxa1, taxa2):
    print('---------------------------')
    print('      RESUMO DO VALOR      ')
    print('---------------------------')
    print(f'Preço analizado: {moeda(p)}')
    print(f'Dobro do preço:  {dobro(p)}')
    print(f'Metade do preço: {metade(p)}')
    print(f'80% de aumento:  {aumentar(p, taxa1)}')
    print(f'35% de redução:  {diminuir(p, taxa2)}')
    print('---------------------------')
