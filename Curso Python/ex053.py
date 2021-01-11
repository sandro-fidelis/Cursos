f = str(input('Digite uma frase: '))
f = f.replace(" ", "")
print(f)
i = f [::-1]
print(i)
if f == i:
    print('Esta frase é um PALINDROMO')
else:
    print('Esta frase NÃO é um palindromo')