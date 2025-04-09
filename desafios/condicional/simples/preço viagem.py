km = float(input('quantos km a viagem '))

if km >= 200:
    km = float(km*0.50)
    print ('custara {:.2f} reais' .format(km))
else:
    km = float(km*0.45)
    print ('custara {:.2f} reais' .format(km))