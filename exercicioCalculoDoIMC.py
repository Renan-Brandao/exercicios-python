nome = 'Renan Almeida Brandão'
altura = 1.84
peso = 85
imc = float(peso / (altura * altura))

print(nome + ' tem ' + str(altura) + ' de altura, pesa ' + str(peso) +' quilos e seu IMC é ' + str(imc)) # Não dá para concatenar string com número diretamente — você precisa converter para string antes:

# Outro exemplo: 

print(f"{nome} tem {altura} de altura, pesa {peso} quilos e seu IMC é {imc:.2f}") # Utilizando F string #mais fácil rs
