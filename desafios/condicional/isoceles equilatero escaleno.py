re1 = float(input ('reta1 '))
re2 = float(input ('reta2 '))
re3 = float(input ('reta3 '))
pode = 0

if (re1+re2 > re3) and (re1+re3 > re2) and (re2+re3 > re1):
    print('pode formar um triangulo')
    pode = 1
else:
    print('nao da nao')

if re1 == re2 == re3 and pode == 1:
    print('equilatero')

elif re1==re2 or re2==re3 or re3==re1 and pode==1:
    print('isóceles')

elif re1 != re2 != re3 and pode==1:
    print('escalano')