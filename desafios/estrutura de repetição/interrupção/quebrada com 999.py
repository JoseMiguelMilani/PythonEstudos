soma = numero = quantia = 0

while True: #repetição infinita
    numero = int(input('digite um numero: '))

    if numero == 999: #interrupção
        break

    soma += numero   #defini quantia e soma
    quantia += 1

print(f'a soma dos {quantia} numeros deu {soma}')