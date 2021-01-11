from datetime import date
a = int(input('Digite o ano desejado, ou digite 0 para analizar o ano atual: '))
if a == 0:
    a = date.today().year
if a%400==0 or a%100!=0 and a%4==0:
    print('O ano {} é Bissexto'.format(a))
else:
    print('O ano {} não é Bissexto'.format(a))
