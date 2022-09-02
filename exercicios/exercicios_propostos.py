numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero = int(numero)

    if numero % 2 == 0:
        print(f'{numero} é par!')
    else:
        print(f'{numero} é impar')

else:
    print(f'Isso não é um número inteiro.')

print('='*50)

horario = input('Digite um horário entre 0 e 23: ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print(f'Por favor digite um horário entre 0 e 23')
    else:
        if horario <= 11:
            print(f'Bom dia!')
        elif horario <= 17:
            print(f'Boa tarde!')
        else:
            print(f'Boa noite!')
else:
    print(f'Por favor digite um horário entre 0 e 23')

print('='*50)

nome = input('Digite seu nome: ')
tamanho = len(nome)

if nome.isalpha():
    nome = str

    if tamanho <= 4:
        print(f'Seu nome é curto')
    elif tamanho <= 6:
        print(f'Seu nome é mediano')
    else:
        print(f'Seu nome é grande')
else:
    print(f'Isso não é um nome')
