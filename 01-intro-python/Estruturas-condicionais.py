# if, if/else, if/elif/else, ternario, match

#if
#if condicao:
#    codigo do if
#    codigo do if
#codigo

idade = 20
if idade >= 18:
    print('maior')

print('fora do if')

# if/else
idade = 20
if idade >= 18:
    print('maior')
else:
    print('menor')

#elif
# crianca 0 12, adolescente 13 17, adulto 18 59, idoso 60+
idade = 30
if idade <= 12:
    print()
elif idade <= 17:
    print()
elif idade <= 59:
    print()
else:
    print()

# evitar alinhamento de ifs
email = ''
senha = ''

if email == 'admin@email.com':
    if senha == '123admin':
        print('liberado')
    else:
        print('email ou senha incorreto')
else:
    print('email ou senha corretos')

    
if email == 'admin@email.com' and senha == '123admin':
    print('liberado')
else:
    print('email ou senha corretos')

# entrada numero 1, 2, 3... 7
# saida dia: Domingo, SEgunda, Terça... Sábado



#operador ternario

if idade >= 18:
    status = 'maior'
else:
    status = 'menor'

status = 'maior' if idade >= 18 else 'menor'

#usuario passa o dia (int)
#devolve string nome 
# 1 - domingo, 2 - segunda... 7 - sabado

dia = 4

dias ={
    1: 'Domingo',
    2: 'segunda',
    3: 'terça',
    4: 'quarta',
    5: 'quinta',
    6: 'sexta',
    7: 'sábado',
}


if dia in dias:
    print(dias(dia))

dia = 2
match dia:
    case 1: 
        print('DOmingo')
    case 2: 
        print('segunda')
    case 3: 
        print('terça')
    case 4: 
        print('quarta')
    case 5: 
        print('quinta')
    case 6: 
        print('sexta')
    case 7: 
        print('sábado')
    case _: 
        print('inválido')

match dia:
    case 1 | 7:
        print('Fim de semana')
    case 2 | 3 | 4 | 5 | 6:
        print('dia útil')
    case _:
        print('inválido')


