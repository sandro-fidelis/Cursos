s = d = 0
while True:
  n = int(input('Digite um número ou [999] para encerrar: '))
  if n == 999:
    break
  d = d + 1 # valores digitados
  s = s + n
print(f'A soma dos {d} números digitados é {s}')