vac = float(input(' valor da casa \033[33m'))
sal = float(input('\033[m salario \033[33m'))
ano = float(input('\033[m quantos anos \033[33m'))

vame = vac/(ano*12)
sald = sal*0.30


print('voce tera que pagar {:.2f} todo mes' .format(vame))

if vame >= sald :
    print('{} negado' .format('\033[31m'))
else :
    print('aceito \033[m')