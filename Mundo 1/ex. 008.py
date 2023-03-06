#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite o valor em metros para realizar a conversão: '))
k = n/1000
h = n/100
d = n/10
dm = n*10
c = n*100
m = n*1000
print('Convertendo {} metros para as outras medidas: \n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(n, k, h, d, dm, c, m))