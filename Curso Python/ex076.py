print('='*40)
print('{:^40}'.format('LISTA DE PREÇOS'))
print('='*40)
p = ('CAMISA', 30.00, 'CANECA', 25.00, 'MOUSE PAD', 15.00,
     'SQUEEZE', 35.00, 'FANTASIA', 90.00, 'LAÇO', 12.00)
print(f'{p[0]:.<32}R$ {p[1]:.2f}')
print(f'{p[2]:.<32}R$ {p[3]:.2f}')
print(f'{p[4]:.<32}R$ {p[5]:.2f}')
print(f'{p[6]:.<32}R$ {p[7]:.2f}')
print(f'{p[8]:.<32}R$ {p[9]:.2f}')
print(f'{p[10]:.<32}R$ {p[11]:.2f}')
print('='*40)


#GUANABARA
print('='*40)
print('{:^40}'.format('LISTA DE PREÇOS'))
print('='*40)
p = ('CAMISA', 30.00, 'CANECA', 25.00, 'MOUSE PAD', 15.00,
     'SQUEEZE', 35.00, 'FANTASIA', 90.00, 'LAÇO', 12.00)
for pos in range(0,len(p)):
     if pos % 2 == 0:
          print(f'{p[pos]:.<30}',end = '')
     else:print(f'R${p[pos]:>7.2f}')
print('='*40)
