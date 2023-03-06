#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um numero: '))
print('O dobro do seu numero é {}, o seu triplo é {}, e sua raiz quadrada é {:.2}'.format(numero*2, numero*3, numero**(1/2)))