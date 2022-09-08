# - Desafio 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1,00 = R$3,27

r = float(input('Quantos reais você tem na sua carteira? '))
d = 3.27
c = r//d
print(f'Com a quantia de R${r}0 , você poderia comprar US${c}0 .')
