vel = int(input('velocidade ') )

if vel > 80:

    acima = int(vel-80)
    paga = int(acima*7)

    print('voce esta {} acima da velocidade, logo pagara {}'.format(acima, paga))
else:
    print('esta tudo certinho')
