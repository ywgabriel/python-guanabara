# - Exercício 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ 1,00 = R$ 5,25

dinheiro = float(input('Quanto dinheiro você tem na carteira? R$ '))
conversao = dinheiro / 5.25
print(f'Com R$ {dinheiro:.2f} você pode comprar US$ {conversao:.2f}')
