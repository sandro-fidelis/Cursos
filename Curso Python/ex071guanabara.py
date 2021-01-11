print('=' * 30)
print('{:^30}'.format('BANCO CENTRAL'))
print('=' * 30)
total = 0
ced = 50
v = int(input('Qual valor quer sacar? R$ '))
total = v
totced = 0
while True:
  if total >= ced:
    total = total - ced
    totced = totced + 1
  else:
    if totced > 0:
      print(f'Total de {totced} cédulas de R$ {ced} Reais')
    if ced == 50:
      ced = 20
      totced = 0
    elif ced == 20:
        ced = 10
        totced = 0
    elif ced == 10:
        ced = 1
        totced = 0
    if total == 0:
         break
print('=' * 30)
print('O banco central agradece. Volte Sempre!')