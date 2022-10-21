

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista1.extend(lista2)

print(lista1)
print(lista2)



print('#'*20)


secreta = 'melancia'
digitadas = []
chances = 5

while True:
    if chances == 0:
        print('Você perdeu! Suas chances se esgotaram.')
        break

    letra = input('Digite uma letra:')

    if len(letra) > 1:
        print('Você deve digitar apenas uma letra!')
        continue

    digitadas.append(letra)

    if letra in secreta:
        print(f'Parabéns! A letra "{letra}" está na palavra secreta.')
    else:
        print(f'Que pena! A letra "{letra}" não está na palvra secreta.')
        digitadas.pop()

    revelacao = ''
    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            revelacao += letra_secreta
        else:
            revelacao += '_'
    if revelacao == secreta:
        print('Incrível! Você ganhou!')
        print(f'A palavra secreta era: {secreta}')
        break
    else:
        print(f'{revelacao}')

    if letra not in secreta:
        chances -= 1
        print(f'Você ainda tem {chances} chances')
