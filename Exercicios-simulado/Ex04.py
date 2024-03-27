'''
Simulador de Eleições: Crie um programa que simule uma votação com três candidatos. 
O programa deve pedir ao usuário para votar várias vezes e, no final, mostrar o número de votos de cada candidato e quem foi o vencedor. 

'''

def simulador_eleicoes():
    candidatos = {'Candidato 1': 0, 'Candidato 2': 0, 'Candidato 3': 0}

    while True:
        print("\nEscolha o seu candidato para votar (ou digite '0' para encerrar a votação):")
        print("1 - Candidato 1")
        print("2 - Candidato 2")
        print("3 - Candidato 3")
        print("0 - Encerrar votação")

        voto = input("Digite o número correspondente ao seu candidato: ")

        if voto == '0':
            break
        elif voto in ('1', '2', '3'):
            candidato = 'Candidato ' + voto
            candidatos[candidato] += 1
            print("Voto registrado para", candidato)
        else:
            print("Opção inválida. Por favor, escolha um número válido.")

    print("\nResultado da votação:")
    for candidato, votos in candidatos.items():
        print(candidato + ": " + str(votos) + " votos")

    maior_votos = 0
    vencedor = ""
    for candidato, votos in candidatos.items():
        if votos > maior_votos:
            maior_votos = votos
            vencedor = candidato

    print("\nO vencedor é:", vencedor)

simulador_eleicoes()
