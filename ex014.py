# - Exercício 014
# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

graus = float(input('Informe a temperatura em °C: '))
fahrenheit = graus * (9 / 5) + 32
print(f'A temperatura de {graus} °C corresponde a {fahrenheit} °F.')
