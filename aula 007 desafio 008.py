# - Desafio 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = int(input('Digite aqui o valor em metros(m): '))
cm = m * 100
mm = m % 1000
print(f'O valor em centímetros(cm) será de: {cm} cm')
print(f'O valor em milímetros(mm) será de: {mm} mm')
