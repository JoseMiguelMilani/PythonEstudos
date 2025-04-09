numero = tabuada = 0
contador = 1

while True: #repetiçao infinita
     numero = int(input('quer ver a tabuada de qual numero:'))

     if numero < 0 :
         print(f'{numero} é negativo, da não')
         break

     print('-'*20)

     for i in range(0,10):
        print(f'{numero} x {contador} = {numero*contador}')
        contador += 1

     print('-'*20)
