from datetime import date
da = date.today()
an = int(input('Digite o ano de seu mascimento? '))
i = da.year - an
print('Quem nasceu em {} tem {} anos em {}.'.format(an,i,da.year))
if i < 18:
    f = 18 - i
    ai = da.year + f
    print('Ainda não é hora de se alistar')
    print('ainda faltam {} anos para poder se alistar'.format(f))
    print('Seu alistamento será em {}'.format(ai))
elif i == 18:
    print('Está na hora de se alistar IMEDIATAMENTE')
elif i > 18:
    f = i - 18
    ai = da.year - f
    print('Já passou o tempo do alistamento')
    print('Você já devia ter se alistado há {} anos atrás'.format(f))
    print('Seu alistamento deveria ter sido feito em {}'.format(ai))

