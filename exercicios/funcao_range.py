
for n in range(10):
    print(n)

#Outro exemplo#

for n in range(5, 15, 2):
    print(n)

print('#'*20)



texto = 'Python'
nova_str = ''

for letra in texto:
    if letra == 't':
        nova_str = nova_str + letra.upper()
    elif letra == 'h':
        nova_str = nova_str + letra.upper()
    else:
        nova_str += letra
print(nova_str)
