from random import randint
j = int()
cont = 0
c = randint(1,10)
print('Pensei em um número entre 0 e 10. ')
while c != j:
  j= int(input('Qual é o seu palpite: '))
  cont += 1
  if c > j:
    print('Dica: O número é maior. ')
  elif c < j:
    print('Dica: O número é menor. ')
  else:
    print('ACERTTOUUU!!!, Voçê acertou na {}° tentativa'.format(cont))
