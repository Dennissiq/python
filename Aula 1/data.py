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