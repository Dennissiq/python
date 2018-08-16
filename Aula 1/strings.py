str1 = input('Digite algum texto\n')
str2 = input('Digite outro texto\n')


print('Tamanho de "{}": {} caracteres'.format(str1, len(str1)))
print('Tamanho de "{}": {} caracteres\n'.format(str2, len(str2)))

if len(str1) == len(str2):
    print('As duas strings possuem o mesmo tamanho')
else:
    print('As duas strings possuem tamanhos diferentes')

if str1 != str2:
    print('As strings possuem conteúdo diferente')
else:
    print('As strings são iguais')