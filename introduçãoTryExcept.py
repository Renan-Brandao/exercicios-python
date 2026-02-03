"""
Introdução ao try/except
try --> Tentar executar o código
except -> Caso ocorra algum erro ao tentar executar
"""

numero_str = input('Digite um valor para calcular o dobro:')

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2}')

except:
    print('O valor digitado não é um número.')