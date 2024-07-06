# Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião, carro e ônibus.
# Levando em consideração:
# ● avião = 600km/h
# ● carro = 100km/h
# ● ônibus = 80km/h

# Velocidades médias em km/h
vel_aviao = 600
vel_carro = 100
vel_onibus = 80

# Recebe a distância da viagem em quilômetros
km_viagem = float(input('Digite os quilômetros de sua viagem: '))

# Calcula o tempo de viagem para cada meio de transporte
tempo_aviao = km_viagem / vel_aviao
tempo_carro = km_viagem / vel_carro
tempo_onibus = km_viagem / vel_onibus

# Converte o tempo de viagem em horas e minutos
horas_aviao = int(tempo_aviao)
minutos_aviao = int((tempo_aviao - horas_aviao) * 60)

horas_carro = int(tempo_carro)
minutos_carro = int((tempo_carro - horas_carro) * 60)

horas_onibus = int(tempo_onibus)
minutos_onibus = int((tempo_onibus - horas_onibus) * 60)

# Exibe os resultados
print('Aqui está o comparativo de sua viagem em horas e minutos:')
print(f'Sua viagem de avião levará: {horas_aviao} horas e {minutos_aviao} minutos')
print(f'Sua viagem de carro levará: {horas_carro} horas e {minutos_carro} minutos')
print(f'Sua viagem de ônibus levará: {horas_onibus} horas e {minutos_onibus} minutos')
