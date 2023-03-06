#Crie um programa que leia dois números e mostre a soma entre eles

valor_1 = int(input('Digite um numero: '))
valor_2 = int(input('Digite outro numero: '))
soma = valor_1 + valor_2

# print('A soma entre', valor_1, 'e', valor_2, 'é', soma)
print('A soma entre {} e {} é {}'.format(valor_1, valor_2, soma))