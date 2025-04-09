homem = idade = sexo = pessoa = mulheres = continuar = 0

while True:

    print('-='*20)

    idade = int(input('idade:\033[32m'))
    sexo = str(input('\033[msexo[M/F]:\033[32m')) 
    if sexo not in 'MF':
        sexo = str(input('\033[msexo[M/F]:\033[32m')) 


    print('-='*20)


    continuar = int(input('\033[mquer continuar\033[32m[1=sim], \033[31m[2]=não\033[m'))


    if sexo == 'M':
        homem +=1

    if idade > 18:
        pessoa += 1

    if sexo == 'F' and idade < 18:
        mulheres += 1

    if continuar == 2:
        break


print('-='*20)
print(f'tem {pessoa} acima dos 18')
print(f'tem {homem} homens')
print(f'tem {mulheres} mulheres abaixo dos 20')
print('-='*20)