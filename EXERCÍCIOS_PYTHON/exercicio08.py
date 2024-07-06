# Solicite ao usuário o número de horas de exercício físico por semana. Calcule o total de calorias queimadas
# em um mês, considerando uma média de 5 calorias por minuto de exercício.

horas_semana1 = float(input('Digite as horas exercitadas na semana 1: '))
horas_semana2 = float(input('Digite as horas exercitadas na semana 2: '))
horas_semana3 = float(input('Digite as horas exercitadas na semana 3: '))
horas_semana4 = float(input('Digite as horas exercitadas na semana 4: '))

total_horas = horas_semana1 + horas_semana2 + horas_semana3 + horas_semana4

cal_por_min = 5
minutos_por_hora = 60
calorias_hora = cal_por_min * minutos_por_hora
total_queimada = total_horas * calorias_hora

print(f'Suas calorias queimadas nesse mes foi de: {total_queimada} calorias. Parabéns!')