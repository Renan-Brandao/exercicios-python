"""
Interpolação básica de string

s - string

%d e %i - int

f - float

x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Renan'
preco = 15487.89
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)