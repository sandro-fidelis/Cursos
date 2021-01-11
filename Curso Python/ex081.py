v = []
while True:
    v.append(int(input('Digite um número: ')))
    cont = str(input('Quer continuar?[S/N] '))
    if cont in 'nN':
        break
print('=' * 40)
print(f'Você digitou estes números {v}')
print(f'Foram digitados {len(v)} números')
v.sort()
print(f'Lista em ordem crescente {v}')
print(f'Lista em ordem decrescente {sorted(v,key = int, reverse=True)}')
if 5 in v:
    print(f'O número 5 existe na lista na posição {v.index(5)} na ordem crescente')
    v.sort(reverse=True)
    print(f'O número 5 existe na lista na posição {v.index(5)} na ordem decrescente')
else:
    print(f'Não existe o número 5 na lista')