# Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima oc onsumo médio em km/l.

quantidade_ltros = float(input('Digite a quantidade de litros de combustivel consumidos:'))
distancia_percorrida = float(input('Agora digite a distancia percorrida:'))

consumo = distancia_percorrida / quantidade_ltros

print(f' O consumo médio de seu veiculo é de: {consumo} km/l')