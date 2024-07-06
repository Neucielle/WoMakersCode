# Faça um Programa que peça dois números, realize as principais operações: soma, subtração, multiplicação e divisão.

num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

print(f'Você digitou o numero {num1} e o número {num2}.\nA soma deles é: {soma}.\nA subtração é: {sub}.\nA multiplicação: {mult}.\nA divisão é: {div}')
