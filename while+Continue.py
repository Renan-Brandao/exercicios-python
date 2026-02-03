"""

Supondo que queira que o código ignore um comando em uma determinada hora do código, podemos utilizar o comando Continue.

"""


contador = 0

while contador <= 50:
    contador+= 1

    if contador == 30:
        continue

    print (contador)