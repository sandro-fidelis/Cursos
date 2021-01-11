from datetime import date

data_atual = date.today()


def voto(nasc):
    idade = data_atual.year - nasc
    if idade >= 18:
        v = 'VOTO OBRIGATÓRIO'
    if idade < 16:
        v = 'NÃO VOTA'
    if idade >= 16 and idade < 18 or idade > 70:
        v = 'VOTO OPCIONAL'
    print(f'Com {idade} anos: {v}')


print('=' * 40)
nasc = int(input('Digite o ano do seu nascimento: '))
voto(nasc)


# GUANABARA

def voto(nasc):
    from datetime import date
    data_atual = date.today()
    idade = data_atual.year - nasc
    if idade >= 18:
        return f'Com idade {idade}: VOTO OBRIGATÓRIO'
    elif idade < 16:
        return f'Com idade {idade}: NÃO VOTA'
    elif idade >= 16 and idade < 18 or idade > 70:
        return f'Com idade {idade}: VOTO OPCIONAL'


print('=' * 40)
nasc = int(input('Digite o ano do seu nascimento: '))
print(voto(nasc))
