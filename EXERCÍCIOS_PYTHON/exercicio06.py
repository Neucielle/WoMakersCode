# Solicite ao usuário o peso em kg e a altura em metros.
# Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula: IMC = peso / (altura * altura).


kg = float(input('Digite seu peso:'))
alt = float(input('Digite sua altura: (ex: 1.65): '))

imc = kg /(alt*alt)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f} e você esta abaixo do peso.')
elif imc >= 18.5 <= imc < 24.9:
    print(f'Seu IMC é de {imc:.1f} e você esta com peso normal.')
elif imc >= 25 <= imc < 29.9:
    print(f'Seu IMC é de {imc:.1f} e você esta com sobrepeso.')
elif imc >= 30 <= imc < 34.9:
    print(f'Seu IMC é de {imc:.1f} e você esta com obesidade grau 1.')
elif imc >= 35 <= imc < 39.9:
    print(f'Seu IMC é de {imc:.1f} e você esta com obesidade grau 2.')
else:
    print(f'Seu IMC é de {imc:.1f} e você esta com obesidade mórbida.')
    
    
    



