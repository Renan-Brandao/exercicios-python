a = 'A'
b = 'B'
c = '1.1'
string = 'a={}, b={}, c={}'

string2 = 'a={0}, b={1}, c={2}' # Passando por índice

string3 = 'a={nome1}, b={nome2}, c={nome3}'


formato1 = string.format(a,b,c)

formato2 = string2.format(a,b,c)

formato3 = string3.format(  #Parâmetro nomeado
    nome1 = a,nome2= b,nome3 = c
    
)

print(formato1)
print(formato2)
print(formato3)