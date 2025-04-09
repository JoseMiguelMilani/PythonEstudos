primeiro = int( input('qual o primeiro termo: ') )
progressao = int( input('qual a progressao:') )
mais = 1

for i in range (0,9):
    if i == 0:
        ari = primeiro + progressao 
        print('{} -- ' .format(ari), end='')
    ari = ari + progressao
    print('{} -- ' .format(ari), end='')


    if i == 8:
        
        while mais != 0:

            mais = int( input('quer mais quantas termos?'))

            for i in range (0,mais):
                ari = ari + progressao
                print('{} -- ' .format(ari), end='')

            if mais == 0:
                print('foram exibidos {} termos' .format(ari/progressao))

   
