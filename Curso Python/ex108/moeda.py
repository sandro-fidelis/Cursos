#MINHA SOLUÇÃO
'''def moeda(p):
    return f'R$ {p:.2f}.replace('.',',')'''''

def moeda(p = 0, moeda = 'R$'):
    return f'{moeda} {p:.2f}'.replace('.',',')

def metade(p=0):
    r = p / 2
    return r

def dobro(p=0):
    r = p * 2
    return r

def aumentar(p=0, taxa=0):
    r = p + ((p * taxa) / 100)
    return r

def diminuir(p, taxa):
    r = p - ((p * taxa) / 100)
    return r
