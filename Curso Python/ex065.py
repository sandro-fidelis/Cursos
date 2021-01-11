r = str('s')
maior = 0
menor = 0
soma = 0
vd = 0
n = 0
media = float(0)
while r == 's':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar: [S/N] '))
    vd = vd + 1
    soma = soma + n
    if vd == 1:
      maior = n
      menor = n
    else:
      if n > maior:
        maior = n
      if n < menor:
        menor = n
media = soma / vd
print('O maior número digitado foi {}'.format(maior))
print('O menor número digitado foi {}'.format(menor))
print('Foram digitados {} números'.format(vd))
print('A soma dos valores digitados é {}'.format(soma))
print('A média entre os valores digitados foi {:.2f}'.format(media))
