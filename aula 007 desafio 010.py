# - Desafio 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ 1,00 = R$ 3,27

reais = float(input('Quantos reais você tem na sua carteira? R$ '))
valor_dolar = 3.27
dolares = reais // valor_dolar
print(f'Com a quantia de R$ {reais:.2f}, você poderia comprar US$ {dolares:.2f}.')
