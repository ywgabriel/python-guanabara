# - Desafio 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual o preço do seu produto? R$  '))
desconto = preco * 0.05
desconto2 = preco * 0.95
print(f'Seu produto com um desconto de 5% vai custar: R$ {desconto2:.2f}.')
