def moeda(p = 0, moeda = 'R$'):
    """
    -> Formata o preço, mudando visualmente.
    :param p: preço digitado pelo usuário
    :param moeda: coloca o 'R$' antes do preço
    :return: retorna a foramtação da 'moeda' e 'p'
    """
    return f'{moeda} {p:.2f}'.replace('.',',')


def metade(p=0, show = False):
    """
    -> Mostra a metade do valor digitado pelo usuário
    :param p: recebe o valor digitado pelo usuário
    :param show: mostra ou não a formatação
    :return:
    """
    r = p / 2
    if show == True:
        return moeda(r)
    else:
        return r


def dobro(p=0, show = False):
    """
    -> Mostra o dobro do valor digitado pelo usuário
    :param p: recebe o preço digitado pelo usuário
    :param show: mostra ou não a formatação
    :return:
    """
    r = p * 2
    if show == True:
        return moeda(r)
    else:
        return r

def aumentar(p=0, taxa=0, show = False):
    r = p + ((p * taxa) / 100)
    if show == True:
        return moeda(r)
    else:
        return r

def diminuir(p, taxa, show = False):
    r = p - ((p * taxa) / 100)
    if show == True:
        return moeda(r)
    else:
        return r

'''
#GUANABARA

def aumentar(p= 0, taxa = 0, formato = False):
    res = p + (p * taxa /100)
    return res if formato == False else moeda(res)


def diminuir(p = 0, taxa = 0, formato = False):
    res = p - (p * taxa /100)
    return res if formato == False else moeda(res)

def dobro(p=0, formato = False):
    res = p * 2
    return res if not formato else moeda(res)# outra forma de escrever o código

def metade(p=0, formato = False):
    res = p / 2
    return res if not formato else moeda(res)

def moeda(p=0, moeda='R$'):
    return f'{moeda} {p:.2f}'.replace('.',',')'''
