pt = int( input('primeiro termo:'))

razao = int(input('qual a razão:'))

for c in range(0, 11):
    soma = pt+(c-1)*razao
    print(soma)
