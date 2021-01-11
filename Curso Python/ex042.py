l1 = float(input('Digite a primeira medida: '))
l2 = float(input('Digite a segunda medida: '))
l3 = float(input('Digite a terceira medida: '))
if (l1 + l2) > l3 and (l2 + l3) > l1 and (l1 + l3) > l2:
    print('Com estas medidas pode ser formado um TRIÂNGULO')
    if l1 == l2 and l1 == l3 and l2 == l3:
        print('Este triângulo é EQUILÁTERO')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Este triâmgulo é ISÓSCELES')
    else:
        print('Este triângulo é ESCALENO')
else:
    print('Com estas medidas NÃO pode se formar um TRIÂNGULO')


