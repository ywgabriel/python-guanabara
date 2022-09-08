# - Desafio 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Qual o preço do seu produto (em R$)? '))
d = p*0.05
d2 = p*0.95
print(f'Seu produto com um desconto de 5% vai custar: R${d2}0 .')
