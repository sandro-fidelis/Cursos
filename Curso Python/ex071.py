print('=' * 30)
print('{:^30}'.format(' BANCO CENTRAL '))
print('=' * 30)
v = int(input('Qual valor você deseja sacar? R$ '))
if v / 50:
  n50 = v / 50
  v = v % 50
  if v / 20:
    n20 = v / 20
    v = v % 20
    if v / 10:
      n10 = v / 10
      v = v % 10
      if v / 1:
        n1 = v / 1
        v = v % 1
if n50 >= 1:
  print(f'Total de {int(n50)} cédulas de 50 Reais')
if n20 >= 1:
  print(f'Total de {int(n20)} cédulas de 20 Reais')
if n10 >= 1:
  print(f'Total de {int(n10)} cédulas de 10 Reais')
if n1 >= 1:
  print(f'Total de {int(n1)} cédulas de 1 Real')
print('=' * 30)
print('O Banco central agradece. Volte Sempre!')