# - Desafio 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Qual o preço do seu produto? R$  '))
desconto = preço * 0.05
desconto2 = preço * 0.95
print(f'Seu produto com um desconto de 5% vai custar: R$ {desconto2:.2f}.')
