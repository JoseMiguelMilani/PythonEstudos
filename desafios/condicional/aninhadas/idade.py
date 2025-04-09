ida = int(input('qual sua idade '))

if ida <= 9 :
    print('mirim')
elif ida <= 14 :
    print('infantil')
elif ida <= 19 :
    print('junior')
elif ida == 20 :
    print('senior')
else:
    print('master')