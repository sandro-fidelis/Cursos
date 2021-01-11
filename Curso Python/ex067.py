while True:
  c = 1
  t = int(input('Quer ver a tabuada de qual número: '))
  if t < 0:
    break
  print('='*11)
  while c <= 10:
    print(f'{t} X {c} = {t*c}')
    c = c + 1
  print('='*11)
print('Programa Tabuada ENCERRADO COM SUCESSO: ')