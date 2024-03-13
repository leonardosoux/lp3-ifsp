# Função
# Modularizar o programa
# reuso
# Manutenabilidade (correçaõ de erros e novas funcionalidades)

# Declaração
def ola_mundo():
    print('Olá mundo')

# chamada
ola_mundo()

# função sem retorno
# side effect - Efeito colateral
def imprimir_mensagem(nome):
    print(f"Bom dia, {nome}")

imprimir_mensagem('José')

# função com retorno
# função pura
def mensagem(nome):
    return f"Bom dia, {nome}"

print(mensagem('Maria'))
# enviar_email(mensagem('Maria'))

#Parâmetro e Argumentos
# Parametro é o que está dentro da função e pode receber argumento (some se fosse um atributo)
def somar(numero1, numero2):
    return numero1 + numero2

somar(1,4)

# Escopo de variáveis
def media(nota1, nota2, nota3):
    total = nota1 + nota2 + nota3
    return total / 3

print(media(8.0, 7.0, 10.0))

# print(total) -> não é possível acessar variaveis criadas na função, fora dela

# Parâmetros com valor padrão
def mensagem(nome, mensagem='Bom dia'):
    return f"{mensagem}, {nome}"

mensagem('MArcos', 'Bom dia')
mensagem('Katia', 'Boa Noite')
mensagem('Pedro')

# Argumentos nomeados
print('Olá mundo', '123', 'teste', sep='@', end="\n\n")
print('TESTE')

mensagem(nome='Lucas', mensagem='Booa Tarde')
mensagem(mensagem='Booa Tarde', nome='Lucas')

# docstring
# comentário de documentação
def somar(n1,n2):
    '''
    Função que soma dois numeros
    :param n1: primeiro número
    :param n2: segundo número
    :return: coma dos números
    '''
    return n1 + n2

# Funções built-in
# print, type, len, sum. min, max, input
# ver no python interativo terminal

def media(*notas):
    return sum(notas) / len(notas)

print(media(10.0))
print(media(10.0, 3.5, 7.5, 3.4))
print(media(10.0, 3.5, 7.5))



