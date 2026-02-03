# Operadores in e not in - Verifica se o valor está entre algo
# Strings são iteráveis, por exemplo:
# 0 1 2 3 4 
"""
nome = 'Renan' # Printando o valor a do nome Renan
print(nome[3])
print('a' in nome)
print('zav' in nome)
print('zav' not in nome)
"""

nome = input('Digite o seu nome: ')
encontrar = input('Digite o caracter que deseja encontrar no seu nome: ')

if encontrar in nome:
    print (f'{encontrar} está presente no seu nome.')

else:
    print(f'{encontrar} não está no seu nome.')