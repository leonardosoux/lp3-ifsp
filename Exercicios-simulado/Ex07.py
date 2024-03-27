'''
Jogo da Forca: Implemente uma versão simples do jogo da forca. O programa começa com uma palavra oculta 
(o usuário não vê) e o usuário tenta adivinhar a palavra, letra por letra.
O usuário tem um número limitado de tentativas para adivinhar toda a palavra.

'''
import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "jogo", "teclado", "mouse", "desenvolvimento"]
    return random.choice(palavras)

def mostrar_forca(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

def jogar_forca():
    palavra = escolher_palavra()
    letras_corretas = set()
    tentativas = 6

    print("Bem-vindo ao jogo da forca!")
    print("Adivinhe a palavra:")
    mostrar_forca(palavra, letras_corretas)

    while tentativas > 0:
        tentativa = input("Digite uma letra: ").lower()

        if tentativa in letras_corretas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if tentativa in palavra:
            letras_corretas.add(tentativa)
            print("Boa! Essa letra está na palavra.")
        else:
            tentativas -= 1
            print("Essa letra não está na palavra. Você tem", tentativas, "tentativas restantes.")

        mostrar_forca(palavra, letras_corretas)

        if all(letra in letras_corretas for letra in palavra):
            print("Parabéns! Você acertou a palavra:", palavra)
            break

    else:
        print("Você perdeu! A palavra era:", palavra)

jogar_forca()
