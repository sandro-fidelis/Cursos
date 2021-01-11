s = float(input('Qual o valor do salário: '))
if s > 1250:
    s1=float(s * 10 / 100) + s
    print('O novo salário deste funcionário será R${:.2f}'.format(s1))
else:
    s1=float(s * 15 / 100) + s
    print('O novo salário deste funcionário será R${:.2f}'.format(s1))
