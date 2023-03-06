#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota_1 = int(input('Digite a primeira nota do aluno: '))
nota_2 = int(input('Digite a segunda nota do aluno: '))
nota_3 = int(input('Digite a terceira nota do aluno: '))

print('A média é {:.3}'.format((nota_1+nota_2+nota_3)/3))
