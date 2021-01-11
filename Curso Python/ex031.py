k = float(input('Quanto Kms vai ter a sua viagem? '))
if k < 200:
    v = k * 0.50
    print('O valor a ser pago por essa viagem é R${:.2f} Reais'.format(v))
else:
    v = k * 0.45
    print('O valor a ser pago por essa viagem é R${:.2f} Reais'.format(v))
