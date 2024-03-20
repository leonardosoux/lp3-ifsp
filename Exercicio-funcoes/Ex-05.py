"""

Crie um programa em Python que solicita ao usuário um identificador 
e apresenta se o que foi informado é um valor válido ou inválido

"""


def verificador(codigo):
    if len(codigo) != 7:
        return False
    
    if codigo[0:2] != "BR" or codigo[6] != "X":
        return False
    
    numero = int(codigo[2:6])
    if numero < 1 or numero > 9999:
        return False
    
    return True
    
codigo = input("Insira seu codigo: ")
    
if verificador(codigo) == True:
    print("seu código é válido")
else:
    print("seu código é invalido")
