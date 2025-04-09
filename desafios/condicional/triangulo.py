re1 = float(input ('reta1 '))
re2 = float(input ('reta2 '))
re3 = float(input ('reta3 '))

if (re1+re2 > re3) and (re1+re3 > re2) and (re2+re3 > re1):
    print('pode formar um triangulo')
else:
    print('nao da nao')