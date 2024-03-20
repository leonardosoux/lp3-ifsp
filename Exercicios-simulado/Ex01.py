'''
Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. 
Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.

'''
import random

def jogo_adivinhacao():
    numero= random.randint(1, 100)
    tentativas = 0

    print("Tente adivinhar um número entre 1 e 100.")

    while True:
        palpite = int(input("Digite seu palpite: "))

        if palpite < numero:
            print("Seu palpite está baixo. Tente novamente!")
        elif palpite > numero:
            print("Seu palpite está alto. Tente novamente!")
        else:
            print(f" Você acertou o número {numero} em {tentativas} tentativas!")
            break

if __name__ == "__main__":
    jogo_adivinhacao()


