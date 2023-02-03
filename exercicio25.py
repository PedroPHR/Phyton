from unidecode import unidecode

print('Responda as perguntas a seguir com [Sim] ou [Nao]')

pergunta1 = str(input('Telefonou para a vítima?: '))
pergunta2 = str(input('steve no local do crime?: '))
pergunta3 = str(input('Mora perto da vítima?: '))
pergunta4 = str(input('Devia para a vítima?: '))
pergunta5 = str(input('Já trabalhou com a vítima?: '))

resp1 = 0
reps2 = 0
resp3 = 0
reps4 = 0
resp5 = 0

x1 = pergunta1.upper()
x2 = pergunta2.upper()
x3 = pergunta3.upper()
x4 = pergunta4.upper()
x5 = pergunta5.upper()

x1 = unidecode(x1)
x2 = unidecode(x2)
x3 = unidecode(x3)
x4 = unidecode(x4)
x5 = unidecode(x5)


if (x1 == 'SIM'):
    resp1 = 1
elif (x1 == 'NAO'):
    resp1 = 0

if (x2 == 'SIM'):
    resp2 = 1
elif (x2 == 'NAO'):
    resp2 = 0

if (x3 == 'SIM'):
    resp3 = 1
elif (x3 == 'NAO'):
    resp3 = 0

if (x4 == 'SIM'):
    resp4 = 1
elif (x4 == 'NAO'):
    resp4 = 0

if (x5 == 'SIM'):
    resp5 = 1
elif (x5 == 'NAO'):
    resp5 = 0

resp_total = resp1 + resp2 + resp3 + resp4 + resp5


if (resp_total == 2):
    print('Você é suspeito')
elif (resp_total > 2 and resp_total < 5):
    print('Você é cumplice')
elif (resp_total == 5):
    print('Você é o assassino')
else:
    print('Você é inocente')
