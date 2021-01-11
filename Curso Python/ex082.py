v = []
p = []
i = []
while True:
    v.append(int(input('Digite um valor: ')))
    cont = str(input('Quer continuar? [S/N]'))
    if cont in 'Nn':
        break
for c in v:
    if c % 2 == 0:
        p.append(c)
    if c % 2 == 1:
        i.append(c)
print('='* 40)
print(f'A lista completa é {v}')
print(f'A lista de pares é {p}')
print(f'A lista de inpares é {i}')
