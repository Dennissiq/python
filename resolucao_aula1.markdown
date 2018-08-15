
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
