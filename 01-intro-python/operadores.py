#Operadores
# aritmédicos
# +, -, /, *, %,

nota1= 10
nota2= 3
media = (nota1 + nota2) / 1 

#potencia
numero = 2 ** 3 # elevado ao cubo
numero = 10 ** 2 # elevado ao quadrado

# lógicos
# and, or, not
# acesso liberado = nao bloqueado, idade > 18, horario comercial
bloqueado = False
idade = 21
hora_atual = 10

horario_comercial = hora_atual >= 8 and hora_atual <= 18
maior_idade = idade >= 18

if not bloqueado and maior_idade and horario_comercial:
    print('liberado')
else:
    print('não liberado')

# operadores de comparação
# >, <, >=, <=, ==, =!

numeros = [1, 2, 3]
numeros2 = [1, 2, 3]

print(numeros == numeros2) # True

# operador is
print(numeros is numeros2) # False
numeros3 = [1, 2]
numeros4 = numeros3
print(numeros3 is numeros4) #True
print(numeros3 is not numeros4) #True

# in (bool)
print('a' in 'python') #false

prontuarios = ['SP001' 'SP002' 'SP003']
prontuario = 'SP002'
print(prontuario in prontuarios) # True

# sim, não, talvez
opcao = ''

if opcao == 'sim' or opcao == 'nao' or opcao == 'talvez':
 print('opcao valida')
else:
 print('opcao invalida') 

opcoes = ('sim', 'nao', 'talvez') 
if opcao in opcoes:
   print('opcao valida')
else:
 print('opcao invalida') 