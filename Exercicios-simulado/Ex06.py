'''
Conversor de Notas Escolares: 
Baseado em uma pontuação fornecida pelo usuário (0 a 100), converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.
'''

pontos = float(input("Digite sua pontuação(de 0 a 100) para converter: "))
 
def conversor_pontos(pontos):
  nota = (pontos * 10) / 100

  
  if nota < 0.0 or nota > 100.0:
        return "Nota inválida"

  if nota >= 9.0:
      return "A"
  if nota < 9.0 and nota >= 7.0:
      return "B"
  if nota < 7.0 and nota >= 5.0:
      return "C"
  if nota < 5.0 and nota >= 1.0:
      return "D"

  return "F"
  
print(f"Nota: {conversor_pontos(pontos)}")