fatorial = int(input('numero:'))

for c in range(1,fatorial):
    
    print('{}*{}' .format(fatorial,c), end='-')
    fatorial=fatorial*c

print('o resultado é {}' .format(fatorial))
