
# coding: utf-8

# # Aula 1
# 
# ## Lista de exercícios - Dennis Siqueira - 81621468

# 1 - Faça um Programa que peça o raio de um círculo, calcule e
# mostre sua área.

# In[7]:


import math

r =  int(input('Insira o raio desejado: \n'))
pi = math.pi
area = pi*(r**2)

print(area)


# 2 - Faça um Programa que calcule a área de um quadrado, em
# seguida mostre o dobro desta área para o usuário.

# In[5]:


l = int(input('Qual o tamanho dos lados do seu quadrado? \n'))

area = l**2
area_2x = area*2

print('A área e: {} \nO dobro da área é: {}'.format(area,area_2x))


# 3 - Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês. Calcule e mostre o total do
# seu salário no referido mês.

# In[6]:


salary_per_hours = int(input('Quanto vc ganha por hora?\n'))
hours_per_month = int(input('Qual a quantidade de horas trabalhadas por mês?\n'))

salary = salary_per_hours * hours_per_month

print('Seu salário é: {}'.format(salary))


# 4 - Faça um Programa que peça a temperatura em graus Farenheit,
# transforme e mostre a temperatura em graus Celsius. C = (5 * (F-
# 32) / 9).

# In[ ]:


f = int(input('Qual a temperatura em Farenheit?\n'))

c = (5*(f-32)/9)

print('a temperatura em celsius é: {}'.format(c))


# 5 - Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Farenheit.

# In[ ]:


c = int(input('Qual a temperatura em Celsius?\n'))

f = (c*1.8)+32

print('a temperatura em Farenheit é: {}'.format(f))


# 6 - Faça um Programa que peça 2 números inteiros e um número
# real. Calcule e mostre:
# - o produto do dobro do primeiro com metade do segundo.
# - a soma do triplo do primeiro com o terceiro.
# - o terceiro elevado ao cubo.

# In[ ]:


num1 = int(input('Insira um número inteiro\n'))
num2 = float(input('Insira um número real\n'))


produto = (2*num1)*(num2/2) 
soma = (num1*3) + produto
terceiro = produto**3

print('O produto do dobro de primeiro é: {}, a soma do triplo é: {}, o terceiro elevado é: {}'.format(produto,soma,terceiro))


# 7 - João Papo-de-Pescador, homem de bem, comprou um
# microcomputador para controlar o rendimento diário de seu
# trabalho. Toda vez que ele traz um peso de peixes maior que o
# estabelecido pelo regulamento de pesca do estado de São Paulo (50
# quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João
# precisa que você faça um programa que leia a variável peso (peso
# de peixes) e verifque se há excesso. Se houver, gravar na variável
# excesso e na variável multa o valor da multa que João deverá pagar.
# Caso contrário mostrar tais variáveis com o conteúdo ZERO.

# In[ ]:


peso = float(input('João, quantos quilos você pescou dessa vez?'))

if peso > 50:
    excesso = peso - 50
    multa =  excesso*4
    print('João, você passou {}kg do limite permitido e pagará R${} de multa'.format(excesso, multa))
else:
    excesso = 0
    multa = 0
    print('João, dessa vez você não pagará nenhuma multa :)\nExcesso: {}\nMulta:{}'.format(excesso,multa))


# 8 - Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês. Calcule e mostre o total do
# seu salário no referido mês, sabendo-se que são descontados 11%
# para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
# faça um programa que nos dê:

# In[8]:


salary_per_hours = int(input('Quanto vc ganha por hora?\n'))
hours_per_month = int(input('Qual a quantidade de horas trabalhadas por mês?\n'))

salary = salary_per_hours * hours_per_month


ir = salary * 0.11
inss = salary * 0.08
syndicate = salary * 0.05

discount = ir + inss + syndicate

liquid_salary = salary - discount

print('O seu salário líquido é R$ {}'.format(liquid_salary))


# 9 -  Faça um programa que leia 2 strings e informe o conteúdo delas
# seguido do seu comprimento. Informe também se as duas strings
# possuem o mesmo comprimento e são iguais ou diferentes no
# conteúdo.

# In[ ]:


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


# 10 - Faça um programa que permita ao usuário digitar o seu nome e
# em seguida mostre o nome do usuário de trás para frente utilizando
# somente letras maiúsculas. Dica: lembre−se que ao informar o
# nome o usuário pode digitar letras maiúsculas ou minúsculas.
# Observação: não use loops.

# In[10]:


nome = input('Digite seu nome\n')

nome = nome[::-1].upper()
print(nome)


# 11 - Faça um programa que solicite a data de nascimento
# (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por
# extenso.
# Data de Nascimento: 29/10/1973
# Você nasceu em 29 de Outubro de 1973.
# Obs.: Não use desvio condicional nem loops.

# In[12]:


bday = input('Quando você nasceu?\n')

mm_ext = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

dd, mm, yyyy = bday.split('/')

print('Você nasceu {} de {} de {}.'.format(dd, mm_ext[int(mm)], yyyy))


# 12 - Leet é uma forma de se escrever o alfabeto latino usando outros
# símbolos em lugar das letras, como números por exemplo. A própria
# palavra leet admite muitas variações, como l33t ou 1337. O uso do
# leet reflete uma subcultura relacionada ao mundo dos jogos de
# computador e internet, sendo muito usada para confundir os
# iniciantes e afrmar-se como parte de um grupo. Pesquise sobre as
# principais formas de traduzir as letras. Depois, faça um programa
# que peça uma texto e transforme-o para a grafa leet speak.
# 
# Desafio: não use loops nem desvios condicionais.
# 

# In[30]:


text = input("Digite seu texto: ")

leetmsg = text

leetwords = "aeiots"
for letter in text:
    if letter in leetwords:
        leetmsg = leetmsg.replace('a', str(4))
        leetmsg = leetmsg.replace('e', str(3))
        leetmsg = leetmsg.replace('i', '!')
        leetmsg = leetmsg.replace('o', str(0))
        leetmsg = leetmsg.replace('t', str(7))
        leetmsg = leetmsg.replace('s', '$')
        
print ("Seu texto l33t é:", leetmsg.upper())

