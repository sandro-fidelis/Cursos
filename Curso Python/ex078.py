n = []
for v in range(0,5):
    n.append(int(input(f'Digite o valor na posição {v}: ')))
print('='*50)
print(f'Você digitou os valores {n}')
print(f'O maior valor digitado foi o {max(n)} nas posições: ',end = '')
for i, v in enumerate(n):
    if v == max(n):
        print(f'{i}...', end = ' ')
print(f'\nO menor valor digitado foi o {min(n)} nas posições: ',end = '')
for i, v in enumerate(n):
    if v == min(n):
        print(f'{i}...', end = ' ')