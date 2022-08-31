nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
idade_menor = 18
idade_maior = 70

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome}, você está apto a pegar um empréstimo!')
else:
    print(f'{nome}, infelizmente você não está apto a pegar um empréstimo.')
