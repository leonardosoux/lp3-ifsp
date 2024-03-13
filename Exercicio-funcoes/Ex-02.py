# Escreva um programa em Python que solicita ao usuário três números e apresenta a média aritmética dos números informados.

n1 = float(input('Digite o primeiro numero'))
n2 = float(input('Digite o segundo numero'))
n3 = float(input('Digite o terceiro numero'))


def media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

mensagem = f"A média aritmética dos números é: {media(n1, n2, n3)}"

