a = float(input('numero 1 '))
b = float(input('numero 2 '))
c = float(input('numero 3 '))

menor=a
if b<c and b<a:
    menor=b
if c<b and c<a:    
    menor=c

maior=a
if b>a and b>c:
    maior=b
if c>b and c>a:
    maior=c

print(maior)
print(menor)