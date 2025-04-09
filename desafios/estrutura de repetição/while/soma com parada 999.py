num, count, soma = 0


while num != 999:

    soma = soma+num
    num = int(input('digite um numero inteiro[999 para parar]'))
    count += 1

if num == 999:
    count -= 1

print('a soma dos {} numeros da {} ' .format(count, soma))