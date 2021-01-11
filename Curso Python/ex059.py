e = 0
maior = int()
while e != 5:
  n1 = int(input('Digite o 1° valor: '))
  n2 = int(input('Digite o 2° valor: '))
  print('''========= MENU =========
Digite [1] SOMAR
Digite [2] MULTIPLICAR
DigIte [3] MAIOR
Digite [4] NOVOS NÚMEROS
Digite [5] SAIR''')
  e = int(input('Qual a sua opção: '))
  if e == 1:
    print('A soma entre {} e {} é {}'.format(n1,n2,n1 + n2))
  if e == 2:
    print('A multiplicação entre {} e {} é {}'.format(n1,n2,n1* n2))
  if e == 3:
    maior = n1
    if n1 < n2:
      maior = n2
      print('O maior número entre {} e {} é {}'.format(n1,n2,maior))
  if e == 4:
    e != 5
  if e > 5 or e == 0 :
    print('ERRO! Opção inváilda: Digite novamente:')
print('SAINDO... FIM')