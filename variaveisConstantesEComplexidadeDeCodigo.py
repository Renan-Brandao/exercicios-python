"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
<- Contagem de complexidade (ruim)
"""
velocidade = 90 # velocidade atual do carro
local_carro = 109 # local em que o carro está na estrada

RADAR_1 = 91 # velocidade máxima do radar 1
LOCAL_1 = 110 # local onde o radar 1 está
RADAR_RANGE = 2 # A distância onde o radar pega
range_radar_1_menor = LOCAL_1 - RADAR_RANGE
range_radar_1_maior = LOCAL_1 + RADAR_RANGE

velocidade_acima_radar_1= velocidade > RADAR_1

#Podemos reescrever o código com melhor legibilidade:
Ultrapassou_range_radar_1 = local_carro >= range_radar_1_menor and local_carro <= range_radar_1_maior

if velocidade_acima_radar_1:
    print('Você está acima da velocidade!')

if velocidade_acima_radar_1 and Ultrapassou_range_radar_1:
    print('Você está acima da velocidade! E multado no radar 1')
else:
    print('Você não foi multado!')