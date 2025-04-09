print ('\033[1;35;45mhello world \033[m')

x=('jose')

print('ola me chamo {}{}{} prazer' .format('\033[32m', x , '\033[m'))

cores = {
    'amarelo': '\033[33m',
    'verde': '\033[32m',
    'limpa': '\033[m'
}

print('Me {}chamo {}{}{}!!!'.format(cores['amarelo'], cores['verde'], x, cores['limpa']))