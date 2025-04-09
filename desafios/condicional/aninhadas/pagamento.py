preco = float(input(' preço? \033[34m'))

tpp = str(input('\033[m tipo de pagamento? a vista ou parcelado? \033[34m')).strip().lower()

#preço a vista

if tpp == 'a vista' or tpp == 'avista':
    avista = (input('\033[m cheque, dinheiro ou cartão? \033[34m')).strip().lower()


    if avista == 'dinheiro' or avista == 'cheque' :
        pagamento = preco-(preco*0.1)

    elif avista == 'cartão' :
        pagamento = preco-(preco*0.05)

    else:
        print('sem desconto, voce pagara {}' .format(preco))

#preço parcelado

elif tpp == 'parcelado' :
    vezes = int(input('\033[m quantas vezes? \033[34m'))

    if vezes == 2:
        pagamento = preco

    elif vezes >= 3:
        pagamento = preco+(preco*(0.2*vezes))

    else:   
        print('entao ai não é parcelado')

print('\033[m voce tera que pagar \033[32m{:.2f} ' .format(pagamento))
