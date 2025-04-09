

for c in range(0,5):
    peso = float(input('qual seu peso '))
    if c == 0:
        leve = peso
        mais = peso
        
    elif peso < leve:
        leve = peso

    elif peso > mais:
        mais = peso

print(leve)
print(mais)