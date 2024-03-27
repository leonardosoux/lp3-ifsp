# Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.



palavra = (input('digite uma palavra'))
palavra = palavra.lower()

vogais = 0
consoantes = 0

for caracter in palavra:
    if caracter in 'aeiou':
        vogais = vogais + 1
    else:
        consoantes = consoantes + 1
         
print ("Vogais:", vogais)
print ("Consoantes:",consoantes)
