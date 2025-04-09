km = float(input('quanto km andou ') )
dia = int( input('quantos dias usou ') )
pre = (dia*60) + (km*0.15)

print ('voce usou por {} dias e andou {}km  logo tera de paga {:.2f}' .format(km, dia, pre))