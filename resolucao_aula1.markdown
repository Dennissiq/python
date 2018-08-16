
# Aula 1

### Lista de exercícios - Dennis Siqueira - 81621468

1 - Faça um Programa que peça o raio de um círculo, calcule e
mostre sua área.

````
import math

r =  int(input('Insira o raio desejado: \n'))
pi = math.pi
area = pi*(r**2)

print(area)
````

2 - Faça um Programa que calcule a área de um quadrado, em
seguida mostre o dobro desta área para o usuário.

````
l = int(input('Qual o tamanho dos lados do seu quadrado? \n'))

area = l**2
area_2x = area*2

print('A área e: {} \nO dobro da área é: {}'.format(area,area_2x))

````

3 - Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total do
seu salário no referido mês.

````
salary_per_hours = int(input('Quanto vc ganha por hora?\n'))
hours_per_month = int(input('Qual a quantidade de horas trabalhadas por mês?\n'))

salary = salary_per_hours * hours_per_month

print('Seu salário é: {}'.format(salary))
````

4 - Faça um Programa que peça a temperatura em graus Farenheit,
transforme e mostre a temperatura em graus Celsius. C = (5 * (F-
32) / 9).

````
f = int(input('Qual a temperatura em Farenheit?\n'))

c = (5*(f-32)/9)

print('a temperatura em celsius é: {}'.format(c))
````

5 - Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Farenheit.

````
c = int(input('Qual a temperatura em Celsius?\n'))

f = (c*1.8)+32

print('a temperatura em Farenheit é: {}'.format(f))
````

6 - Faça um Programa que peça 2 números inteiros e um número
real. Calcule e mostre:
- o produto do dobro do primeiro com metade do segundo.
- a soma do triplo do primeiro com o terceiro.
- o terceiro elevado ao cubo.

````
num1 = int(input('Insira um número inteiro\n'))
num2 = float(input('Insira um número real\n'))


produto = (2*num1)*(num2/2) 
soma = (num1*3) + produto
terceiro = produto**3

print('O produto do dobro de primeiro é: {}, a soma do triplo é: {}, o terceiro elevado é: {}'.format(produto,soma,terceiro))
````

7 - João Papo-de-Pescador, homem de bem, comprou um
microcomputador para controlar o rendimento diário de seu
trabalho. Toda vez que ele traz um peso de peixes maior que o
estabelecido pelo regulamento de pesca do estado de São Paulo (50
quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João
precisa que você faça um programa que leia a variável peso (peso
de peixes) e verifque se há excesso. Se houver, gravar na variável
excesso e na variável multa o valor da multa que João deverá pagar.
Caso contrário mostrar tais variáveis com o conteúdo ZERO.

````
peso = float(input('João, quantos quilos você pescou dessa vez?'))

if peso > 50:
    excesso = peso - 50
    multa =  excesso*4
    print('João, você passou {}kg do limite permitido e pagará R${} de multa'.format(excesso, multa))
else:
    excesso = 0
    multa = 0
    print('João, dessa vez você não pagará nenhuma multa :)\nExcesso: {}\nMulta:{}'.format(excesso,multa))
````

8 - Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total do
seu salário no referido mês, sabendo-se que são descontados 11%
para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
faça um programa que nos dê:

````
salary_per_hours = int(input('Quanto vc ganha por hora?\n'))
hours_per_month = int(input('Qual a quantidade de horas trabalhadas por mês?\n'))

salary = salary_per_hours * hours_per_month


ir = salary * 0.11
inss = salary * 0.08
syndicate = salary * 0.05

discount = ir + inss + syndicate

liquid_salary = salary - discount

print('O seu salário líquido é R$ {}'.format(liquid_salary))
````

9 -  Faça um programa que leia 2 strings e informe o conteúdo delas
seguido do seu comprimento. Informe também se as duas strings
possuem o mesmo comprimento e são iguais ou diferentes no
conteúdo.

````

````