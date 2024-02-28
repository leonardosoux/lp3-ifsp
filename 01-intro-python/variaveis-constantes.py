# identificadores
# letras, número, _
# não pode ser palavra reservada:
# if, for, class ...
# case sensitive
a = 10
A= 10

# variaveis
# identificador = literal (valor)
#snake_case (convenção)
idade = 10 #int
nome = "Kaio" #str
pessoa_juridica = "Google" #str
imposto_renda = 2000.00 #float
verdade = True #boolean

# Constantes
# Valor não muda após definido
# Não existe constante no python
PI = 3.14

# Comentário única linha 

"""comentário múltiplas linhas"""

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