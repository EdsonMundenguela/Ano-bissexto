ano = int(input('Que ano você quer analisar:'))
if ano % 4 == 0:
    print('ano bissexto {}'.format(ano))
else:
    print('o ano nao é bissexto {}'.format(ano))