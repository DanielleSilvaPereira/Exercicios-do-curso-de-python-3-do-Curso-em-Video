#Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

y = input('Digite algo: ')

print('{} É do tipo {}'.format(y, type(y)))

print('{} Só tem espaço?{}'.format(y, y.isspace()))

print('{} Só tem número?{}'.format(y, y.isnumeric()))

print('{} Só tem letra?{}'.format(y, y.isalpha()))

print('{} Tem números e letras?{}'.format(y, y.isalnum()))

print('{} Só tem minúscula?{}'.format(y, y.islower()))

print('{} Só tem maiúscula?{}'.format(y, y.isupper()))
