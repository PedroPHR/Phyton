num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))

print('Qual opção você deseja: ')

print('A --> Par Ou impar')
print('B --> Positivo ou Negativo')
print('C --> Inteiro ou Decimal')

escolha = str(input())

x = escolha.upper()

if (x == 'A'):
    if (num1 % 2 == 0):
        print(f'O numero: {num1} é par')
    else:
        print(f'O numero: {num1} é impar')
    if (num2 % 2 == 0):
        print(f'O numero: {num2} é par')
    else:
        print(f'O numero: {num2} é impar')

if (x == 'B'):

    if (num1 > 0):
        print(f'O numero: {num1} é positivo')
    elif (num1 < 0):
        print(f'O numero: {num1} é Negativo')
    if (num2 > 0):
        print(f'O numero: {num2} é positivo')
    elif (num2 < 0):
        print(f'O numero: {num2} é negativo')
    if (num1 == 0):
        print(f'O numero: {num1} é neutro')
    if (num2 == 0):
        print(f'O numero: {num2} é neutro')

if (x == 'C'):
    if (num1 == round(num1)):
        print('é um numero inteiro')
    else:
        print('é um numero Decimal')
    if (num2 == round(num2)):
        print('é um numero inteiro')
    else:
        print('é um numero Decimal')
