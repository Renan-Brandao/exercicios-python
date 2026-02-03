"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nom é muito grande".
"""
"""
nome_usuario = input('Digite o seu nome: ')

tamanho_nome_usuario = len(nome_usuario)
print(tamanho_nome_usuario)


if tamanho_nome_usuario > 1:
    
    if tamanho_nome_usuario <=4:
        print('Seu nome é curto!')
    elif tamanho_nome_usuario == 5 or tamanho_nome_usuario == 6:
        print('seu nome é normal!')
    else:
        print('Seu nome é muito grande!')

else:
    print('Digite mais de uma letra!')
"""
"""
hora_escolhida = input('Que horas são? ')

try:
    hora = int(hora_escolhida)
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <=17:
        print('Boa tarde!')
    else:
        print('Boa noite!')
except:
    print('O valor digitado está incorreto!')

"""    


numero_string = input('Digite um número inteiro: ')

try:
    numero_inteiro = int(numero_string)
    if numero_inteiro % 2 == 0:
        print('O valor digitado é par!')
    else:
        print('O valor digitado é impar!')

except:
    print('O valor digitado não é um inteiro!')
