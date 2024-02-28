# Tipo de Dados

#N úmerico

# int
idade = 10

# float
altura = 1.65

# Booleano
# True, False 
verdade = True
mentira = False 
ligado = True
frete_gratis = True 


# str = String
# sequencia de caracteres
# literal de str 
nome = "Jóse"
nome = 'José'

# char
letra = "a"

frase = """
Olá Pessoal
teste
teste
"""

# interploração de string
nome = 'Sonia'
idade = 23

#f-string
mensagem = f"Bom dia {nome}. Você tem {idade} anos!"

nome = "Silvio Santos"
print (nome [2])
print (nome [0:3])

# str são objetos
# métodos
print(nome.upper())
print(nome)

# list
# lista de valores 
# pode conter valores de tipos diferentes
# podem ser alterada (adicionar, remover)
habilidades = ['java', 'html', 'css']
print (habilidades [0])

#alterando a list
habilidades[0] = 'javascript'
print(habilidades)

# adicionar no final da lista
habilidades.append('python')
print (habilidades)

#adc em uma posoção
habilidades.insert(0, 'kotlin')
print (habilidades)

# remove, sort, clear, copy...

for habilidade in habilidades:
    print(habilidade)


# tuple
# lista de valores
# não pode mudar os valores
opcoes = ('sim', 'não', 'talvez')
racas_rpg = ('anao', 'humano', 'elfo')

print(opcoes[1])

# função que retorna estastisticas sobre as notas de um aluno
# media, menor nota, maior nota
# entrada: n1, n2, n3 ou notas(list)
# saída: media, menor nota, maior nota
def estatistica_nota(notas):
    media = sum(notas) / len(notas)
    menor = min(notas)
    maior = max(notas)
    return media, menor, maior

notas = [10.0, 5.5, 8.5, 1.8]
estatistica = estatistica_nota(notas)
print(estatistica)

#desempacotando tupla
media, menor, maior = estatistica_nota(notas)
print(media, menor, maior)

# set
# conjunto de valores
# não permite valores duplicados
# não é indexado
habilidades = {'java', 'python', 'css'}
habilidades.add('java')
print(habilidades)

# dict
# dicionario
# palavras
# palavra => definição
# chave => valor
# key => value
nome = "Silvio Santos"
casado = True
idade = 120

pessoa = {
    "nome": "Silvio Santos",
    "casado": True,
    "idade": 120
}

print(pessoa["nome"])
print(pessoa["casado"])
print(pessoa["idade"])

# None
# null
nulo = None
