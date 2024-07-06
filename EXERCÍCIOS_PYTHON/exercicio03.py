# Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros

qntidade_kms = float(input('Digite os quilometros desejados:'))

metros = qntidade_kms * 1000
centimetros = qntidade_kms * 100
milimetros = qntidade_kms * 10


print(f'Os seus km digitados que foi de {qntidade_kms} ficam com:\n {metros:.2f} metros, {centimetros:.2f} cm e {milimetros:.2f}.')
