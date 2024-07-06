# Faça um Programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês. Calcule e mostre o total
# do seu salário no referido mês.

valor_hora = float(input('Digite seu salario por hora: '))
horas_trab = float(input('Agora digite as suas horas trabalhadas no mês: '))

total_salario = horas_trab * valor_hora

print(f'O total de seu salário com base nas horas trabalhadas e valor é de: {total_salario}')
