from datetime import date
atual = date.today()
p = 0
for d in range(0,3):
    data = int(input('Digite a data: '))
    i = atual.year - data
    print(i)
    if i >= 18:
        p = p + 1
print('{} pessoas são maiores de idade'.format(p))
