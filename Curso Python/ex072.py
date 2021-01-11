n = ('zero','um','dois','tres','quatro','cinco','seis','sete', 'oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')
while True:
  cont = ' '
  while cont not in 'NS':
    e = int(input('Digite um número entre 0 e 20: '))
    if e >= 0 and e <= 20:
      break
    print('Número inválido: Tente Novamente.')
  print(f'O número escolhido foi o "{n[e]}"')
  while cont not in 'NS':
    cont = str(input('Quer continuar? ').strip().upper()[0])
  if cont == 'N':
    break
print('FIM DO PROGRAMA')