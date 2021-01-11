v = []
for c in range(0,5):
  n = (int(input('Digite um número: ')))
  if c == 0 or n > v[-1]:
    v.append(n)
    print(f'Valor {n} adicionado na última posição')
    print(v)
    print('=' * 40)
  else:
      pos = 0
      while pos < len(v):
        if n <= v[pos]:
          v.insert(pos,n)
          print(f'Adicionado na posição {pos} da lista')
          print(v)
          print('=' * 40)
          break
        pos += 1
