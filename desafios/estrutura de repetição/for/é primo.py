num = int(input('numero:'))
tot = 0

for i in range (1, num  + 1):
    if num % i == 0:
        tot += 1


print(' o numero {} foi divisivel por {} numeros'. format(num, tot))

if tot == 2:
    print('é primo')

else:
    print('nao é primo')
    

        



        

        

