p = float(input('Digite o seu peso: (Kg) '))
a = float(input('Digite a sua altura: (m) '))
imc = p / (a * a)
print('O IMC desta pessoa é : {:.2f}'.format(imc))
if imc < 18.5:
    print('ABAIXO do peso')
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('SOBREPESO')
elif imc >= 30 and imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
