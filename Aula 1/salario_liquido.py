salary_per_hours = int(input('Quanto vc ganha por hora?\n'))
hours_per_month = int(input('Qual a quantidade de horas trabalhadas por mês?\n'))

salary = salary_per_hours * hours_per_month


ir = salary * 0.11
inss = salary * 0.08
syndicate = salary * 0.05

discount = ir + inss + syndicate

liquid_salary = salary - discount

print('O seu salário líquido é R$ {}'.format(liquid_salary))