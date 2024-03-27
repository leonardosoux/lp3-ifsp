'''
Função de Contagem de Palavras: Escreva uma função que receba uma string (frase) como argumento 
e retorne um dicionário onde as chaves são as palavras únicas no texto e os valores são o número de vezes que cada palavra aparece no texto. 
Depois, teste a função com diferentes textos fornecidos pelo usuário.

'''

def contar_palavras(frase):
    # Remover pontuações e converter todas as palavras para minúsculas
    frase = frase.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace(';', '').replace(':', '')
    # Dividir a frase em palavras individuais
    palavras = frase.split()
    # Inicializar o dicionário para armazenar a contagem de palavras
    contagem = {}
    # Contar o número de ocorrências de cada palavra
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

# Teste da função com diferentes textos fornecidos pelo usuário
texto = input("Digite um texto: ")
resultado = contar_palavras(texto)
print("Contagem de palavras:")
for palavra, contagem in resultado.items():
    print(f"{palavra}: {contagem}")
