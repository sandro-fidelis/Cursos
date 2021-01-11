from time import sleep
def contagem(i, f, p):
  if p < 0:
    p *= -1
  if  p == 0:
    p = 1
  print('=' *40)
  print(f'Contagem de {i} até {f} de {p} em {p}')
  if i < f:
    cont = i
    while cont <= f:
      print(f'{cont}', end = ' ', flush = True)
      sleep(0.5)
      cont += p
    print('FIM')
  else:
    cont = i
    while cont >= f:
      print(f'{cont}',end = ' ', flush =  True)
      sleep(0.5)
      cont -= p
    print('FIM')


contagem(1, 10, 1)
contagem(10, 0, 2)
print('=' *40)
print('Agora é a sua vez de personalizar a contagem')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contagem(i, f, p)