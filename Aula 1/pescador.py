peso = float(input('João, quantos quilos você pescou dessa vez?'))

if peso > 50:
    excesso = peso - 50
    multa =  excesso*4
    print('João, você passou {}kg do limite permitido e pagará R${} de multa'.format(excesso, multa))
else:
    excesso = 0
    multa = 0
    print('João, dessa vez você não pagará nenhuma multa :)\nExcesso: {}\nMulta:{}'.format(excesso,multa))

    
    