n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = float((n1 + n2) / 2)
if m < 5.0:
    print('A nota final foi {:.1f}'.format(m))
    print('SITUAÇÃO : REPROVADO')
elif m > 5.1 and m < 6.9:
    print('A nota final foi {:.1f}'.format(m))
    print('SITUAÇÃO : RECUPERAÇÃO')
elif m >= 7.0:
    print('A nota final foi {:.1f}'.format(m))
    print('SITUAÇÃO : APROVADO')