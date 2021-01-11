from random import randint
s = 0 # soma
vitoria = False
qv = 0#quantidade de vitorias
while True:
  print('='*18)
  print('JOGO PAR OU ÍMPAR')
  print('='*18)
  pi = str(' ')#par ou impar escolha
  j = int(input('Digite seu número: entre [0 e 10]: '))
  while pi not in 'PI':
    pi = str(input('PAR OU ÍMPAR [P/I]: ')).strip().upper()[0]
  c = randint(0,10)#escolha randomica do computador
  s = j + c
  if s % 2 == 0:
    res = 'PAR'
  else:
    res = 'ÍMPAR'
  print(f'computador escolheu {c} e você {j}, total {s}, {res}')
  if s % 2 == 0 and pi == 'P':
    vitoria = True
    qv = qv + 1
    print('VOÇÊ VENCEU!!')
  elif s % 2 == 1 and pi == 'I':
    vitoria = True
    qv = qv + 1
    print('VOÇÊ VENCEU!!')
  else:
    vitoria = False
    print('VOÇÊ PERDEU!!')
  if vitoria == False:
    break
print(f'Voçê venceu {qv} vezes')
print('FIM')