num1 = int(input('Insira um número inteiro\n'))
num2 = float(input('Insira um número real\n'))


produto = (2*num1)*(num2/2) 
soma = (num1*3) + produto
terceiro = produto**3

print('O produto do dobro de primeiro é: {}, a soma do triplo é: {}, o terceiro elevado é: {}'.format(produto,soma,terceiro))