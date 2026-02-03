"""
Flag (Bandeira) - Marcar um local

None = não valor

is e is not = é ou não é - Geralmente utilizado com variáveis de valor None

id = identidade (Local na memória armazenado determinado valor)

"""

name = 'Roberta'

print(id(name)) # Printa o local onde a variável está armazenado na memória.

condicao = True
passou_no_if = None


if condicao:
    passou_no_if = None
    print('Passou no if')
else:
    print('Não passou no if')


if passou_no_if is None:  # is ou is not
    print('if é none')
else:
    print('if não é none')

if passou_no_if is not None:  # is ou is not
    print('if não é none')
else:
    print('if é none')