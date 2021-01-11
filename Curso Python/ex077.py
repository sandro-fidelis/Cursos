p = ('double dragon', 'fifa', 'mario bros', 'final fight', 'street fighter',
     'alien', 'castle of ilusions', 'quack shot', 'sunset riders', 'flashback')
for c in p:
    print(f'\nA palavra {c.upper()} temos as vogais', end = ' - ')
    for letra in c:
        if letra in 'aeiou':
            print(letra, end = ' ')
