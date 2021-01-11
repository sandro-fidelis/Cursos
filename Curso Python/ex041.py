from datetime import date
aa = date.today()
an = int(input('Digite o ano do nascimento do atleta: '))
i = aa.year - an
print('O atleta tem a idade de {} anos'.format(i))
if i <= 9:
    print('Categoria do atleta é MIRIM')
elif i > 9 and i <= 14:
    print('Categoria do atleta é INFANTIL')
elif i > 14 and i <= 19:
    print('Categoria do atleta é JUNIOR')
elif i > 19 and i <= 25:
    print('Categoria do atleta é SÊNIOR')
else:
    print('Categoria do atleta é MASTER')
