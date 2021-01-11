def notas(* resp, sit = False):
    """
    notas(* resp, sit = False)
    -> Função para mostar notas de alunos e situação.
    :param resp: uma ou mais notas dos alunos (pode ser várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com informações sobre os alunos.
    """

    dic = {}
    dic['total'] = (len(resp))
    dic['maior'] = (max(resp))
    dic['menor'] = (min(resp))
    s = 0
    for v in resp:
        s += v
        media = s / len(resp)
        dic['media'] = (f'{media:.2f}')
        if sit == True:
            if media < 6:
              dic['situação'] = 'Ruim'
            if media >= 6 and media < 7:
              dic['situação'] = 'Razoavel'
            if media >= 7 and media < 8:
              dic['situação'] = 'Boa'
            if media >= 8:
              dic['situação'] = 'Ótima'
            return dic



resp = notas(7.5, 6, 2.5, sit =True)
print(resp)
help(notas)
#GUANABARA

def notas(*n, sit = False):
    """
       notas(* resp, sit = False)
       -> Função para mostar notas de alunos e situação.
       :param resp: uma ou mais notas dos alunos (pode ser várias)
       :param sit: valor opcional, indicando se deve ou não adicionar a situação.
       :return: dicionário com informações sobre os alunos.
       """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menos'] = min(n)
    r[f'média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RQZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


#Programa Principal
resp = notas(5.5, 2.5, 1.5, sit = True)
print(resp)