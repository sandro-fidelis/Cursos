from random import randint
v = 0
while True:
  j = int(input('Digite um número: '))
  c = randint(0,10)
  total = j + c
  tipo = ' '
  while tipo not in 'PI':
    tipo = str(input('Escolha PAR ou ÍMPAR [P/I] ')).strip().upper()[0]
  print(f'Voçê escolheu {j} e o computador {c}, total {total}',end ='')
  print(' DEU PAR' if total % 2 == 0 else ' DEU ÍMPAR')
  if tipo == 'P':
    if total % 2 == 0:
      print('Você VENCEU!!!')
      v = v + 1
    else:
      print('Você PERDEU!!!')
      break
  if tipo == 'I':
    if total % 2 == 1:
      print('Você VENCEU!!!')
      v = v + 1
    else:
      print('Você PERDEU!!!')
      break
  print('Vamos jogar novamente...')
print(f'GAME OVER! Você ganhou {v} vezes')
