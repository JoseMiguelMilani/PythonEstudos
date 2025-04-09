preco = total = quantos = continuar = 0
nome = baratonome = ""
barato = 100000

while continuar == 0:
    nome = str(input('produto:'))
    preco = float(input('preço:'))

    total += preco 

    if preco > 1000 :
        quantos += 1

    if preco < barato:
        barato = preco
        baratonome = nome
        

    continuar = int(input('quer continuar? [1]não   [0]sim'))



print(f'o total gasto é {total:.2f}')

print(f'{quantos} produtos custaram mais de 1000')

print(f'o produto mais barato é {baratonome}')


