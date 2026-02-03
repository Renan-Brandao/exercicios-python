"""
Operadores lógicos:
and (e) or (ou) not(não)

and-- Todas as condições precisam ser verdadeiras.
Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele falor.

or - Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.

not - Inverter o valor final das expressões.

Também existe o tipo None que é usado para representar um não valor
"""

entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = int (input('Digite sua senha para o login: '))
senha_permitida = 12345

if (entrada == 'E' or 'e') and senha_digitada == senha_permitida:
    print("Bem vindo!")
   
else:
    print('Você saiu do sistema!')

# Avaliação de curto circuito
# - and - print(True and False and True) # Se a avaliação for definida como False, o programa entenderá como False e a retornará como valor
# - or - print( 0 or False or True) # Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.
# - not - print (not 0 or False or False) # Inverter o valor final das expressões.

